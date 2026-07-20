from __future__ import annotations

import re
from contextlib import contextmanager
from io import StringIO
from typing import Generator, TextIO, TypeAlias, TypeVar

import pyparsing as pp

comma = pp.Literal(",").suppress()
quote = pp.Literal('"').suppress()
open_bracket = pp.Literal(".{").set_name(".{").suppress()
close_bracket = pp.Literal("}").set_name("}").suppress()

simple_identifier = (
    pp.Regex(r"\.\w+").set_parse_action(lambda t: t[0][1:]).set_name("simple_identifier")
)
arbitrary_identifier = (
    pp.Regex(r".@\"[^\"@]*\"").set_parse_action(lambda t: t[0][3:-1]).set_name("complex_identifier")
)
identifier = (simple_identifier | arbitrary_identifier).set_name("any_identifier")

boolean = (
    (pp.Literal("true") | pp.Literal("false"))
    .set_parse_action(lambda t: t[0] == "true")
    .set_name("boolean_literal")
)

null = (
    pp.Literal("null")
    .set_parse_action(
        lambda _: pp.ParseResults([None])
    )  # None would be discarded if returned directly.
    .set_name("null_literal")
)

string = (quote + pp.Regex(r'[^"]*') + quote).set_name("string_literal")

number = (
    (pp.Regex(r"0x[a-fA-F0-9]+").set_parse_action(lambda t: int(str(t[0]), 16))).set_name(
        "hexadecimal_integer_literal"
    )
    | (
        #               x.            .x      x.y
        pp.Regex(r"-?(([0-9]+\.[0-9]+)|([0-9]+\.)|(\.[0-9]+))(?:[eE][+-]?[1-9]+)?")
        .set_parse_action(lambda t: float(str(t[0])))
        .set_name("float_literal")
    )
    | (pp.Regex(r"-?[0-9]+").set_parse_action(lambda t: int(str(t[0]))).set_name("integer_literal"))
)

array = pp.Forward()
struct = pp.Forward()

value = null | boolean | identifier | string | number | struct | array

array <<= (
    pp.Group(
        open_bracket
        + pp.ZeroOrMore(value + comma.suppress())
        + pp.Opt(value + pp.Opt(comma.suppress()))
        + close_bracket
    )
    .set_parse_action(pp.ParseResults.as_list)
    .set_name("array")
)

key_value_pair = pp.Group(
    identifier.set_results_name("key", list_all_matches=True)
    + pp.Literal("=").suppress()
    + value.set_results_name("value", list_all_matches=True)
).set_name("key_value_pair")

struct <<= (
    (
        open_bracket
        + pp.ZeroOrMore(key_value_pair + comma)
        + pp.Opt(key_value_pair + pp.Opt(comma).suppress())
        + close_bracket
    )
    .set_parse_action(lambda t: dict(t.as_list()))
    .set_name("struct")
)

Zon: TypeAlias = "int | str | float | dict[str, Zon] | list[Zon]"


def loads(source: str) -> Zon:
    return value.parse_string(source)[0]  # type: ignore[pylance]


T = TypeVar("T")


class ZonSerializer:
    def __init__(self, io: TextIO, *, do_escape_strings: bool, indent: str) -> None:
        self.io = io
        self.do_escape_strings = do_escape_strings
        self.indent = indent
        self.simple_identifier = re.compile(r"^\w+$")

        self._current_indent_level = 0
        self._current_indent_string = ""

        self._jump_table = {
            type(None): self.on_null,
            bool: self.on_bool,
            int: self.on_int,
            float: self.on_float,
            str: self.on_str,
            dict: self.on_struct,
            list: self.on_array,
        }

    @property
    def _has_indent(self) -> bool:
        return len(self.indent) > 0

    @contextmanager
    def _indent(self) -> Generator[None, None, None]:
        self._current_indent_level += 1
        old = self._current_indent_string
        self._current_indent_string = self.indent * self._current_indent_level

        yield

        self._current_indent_level -= 1
        self._current_indent_string = old

    def on_zon(self, node: object) -> None:
        callback = self._jump_table.get(type(node), self.on_generic_object)
        callback(node)

    def on_generic_object(self, other: object) -> None:
        self.on_struct(other.__dict__)

    def on_null(self, _: None) -> None:
        self.io.write("null")

    def on_bool(self, node: bool) -> None:  # noqa: FBT001
        self.io.write("true" if node else "false")

    def on_int(self, node: int) -> None:
        self.io.write(str(node))

    def on_float(self, node: int) -> None:
        self.io.write(str(node))

    def on_str(self, node: str) -> None:
        if self.do_escape_strings:
            self.io.write(repr(node.encode("utf-8"))[1:])
            return

        self.io.write('"')
        self.io.write(node)
        self.io.write('"')

    def on_identifier(self, node: str) -> None:
        self.io.write(".")

        if self.simple_identifier.match(node):
            self.io.write(node)
            return

        self.io.write('@"')
        self.io.write(node)
        self.io.write('"')

    def on_struct(self, node: dict[str, Zon]) -> None:
        self.io.write(".{")

        with self._indent():
            for i, (key, value) in enumerate(node.items()):
                if self._has_indent:
                    self.io.write("\n")
                    self.io.write(self._current_indent_string)

                self.on_identifier(key)
                self.io.write(" = ")
                self.on_zon(value)

                if i != (len(node) - 1) or self._has_indent:
                    self.io.write(",")

        if len(node) != 0 and self._has_indent:
            self.io.write("\n")
            self.io.write(self._current_indent_string)

        self.io.write("}")

    def on_array(self, node: list[Zon]) -> None:
        self.io.write(".{")

        with self._indent():
            for i, value in enumerate(node):
                if self._has_indent:
                    self.io.write("\n")
                    self.io.write(self._current_indent_string)

                self.on_zon(value)

                if i != (len(node) - 1) or self._has_indent:
                    self.io.write(",")

        if len(node) != 0 and self._has_indent:
            self.io.write("\n")
            self.io.write(self._current_indent_string)

        self.io.write("}")


def dumps(
    zon: object,
    *,
    serializer: type[ZonSerializer] = ZonSerializer,
    do_escape_strings: bool = False,
    indent: str = "",
) -> str:
    dump(
        zon,
        io := StringIO(),
        serializer=serializer,
        do_escape_strings=do_escape_strings,
        indent=indent,
    )
    assert io.seekable()
    io.seek(0)
    return io.read()


def dump(
    zon: object,
    io: TextIO,
    *,
    serializer: type[ZonSerializer] = ZonSerializer,
    do_escape_strings: bool = False,
    indent: str = "",
) -> None:
    serializer(
        io,
        do_escape_strings=do_escape_strings,
        indent=indent,
    ).on_zon(zon)
