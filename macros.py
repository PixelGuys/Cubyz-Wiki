from __future__ import annotations
from pathlib import Path
import sys
import textwrap
from traceback import format_exc
from typing import TYPE_CHECKING

THIS_DIRECTORY = Path(__file__).parent
DATABSE_FILE = THIS_DIRECTORY / "scripts" / "assets.zon"

sys.path.append(THIS_DIRECTORY.as_posix())

from scripts.assetgen2 import ENV, AssetDatabase, Id, load_db_cached

if TYPE_CHECKING:
    from zensical.extensions.macros import MacroEnv

db = load_db_cached(DATABSE_FILE)


def define_env(env: MacroEnv):
    @env.macro
    def item_infobox(id_string: str):
        try:
            id = Id.from_str(id_string)

            if id not in db.items:
                return ""

            item = db.items[id]
            template = ENV.get_template("item_infobox.jinja2.md")
            infobox = template.render(item=item)

            return textwrap.indent(infobox, prefix="    ")
        except Exception:
            return format_exc()

    @env.macro
    def block_infobox(id_string: str):
        try:
            id = Id.from_str(id_string)

            if id not in db.blocks:
                return ""

            block = db.blocks[id]
            template = ENV.get_template("block_infobox.jinja2.md")
            infobox = template.render(block=block)

            return textwrap.indent(infobox, prefix="    ")
        except Exception:
            return format_exc()
