from __future__ import annotations

import argparse
from copy import deepcopy
import sys
from functools import cached_property, lru_cache
from pathlib import Path
from typing import Any, ClassVar, Dict, Self, cast

import jinja2
import pydantic
from scripts import zon


THIS_DIRECTORY = Path(__file__).parent.resolve()
TEMPLATE_DIRECTORY = THIS_DIRECTORY / "templates"
CUBYZ_REPO_RAW_CONTENT_BASE_URL = (
    "https://raw.githubusercontent.com/PixelGuys/Cubyz/refs/tags/0.3.0"
)
DOCS_FOLDER = THIS_DIRECTORY.parent / "docs"

LOADER = jinja2.FileSystemLoader([TEMPLATE_DIRECTORY.as_posix()])
ENV = jinja2.Environment(loader=LOADER)


def main(args: list[str]) -> None:
    config = parse_args(args)

    db: AssetDatabase | None = None

    if config.repo and config.repo.exists():
        db = rebuild_metadata(config)
        if config.db:
            config.db.write_text(db.dump_zon())

    if db is None:
        if config.db and config.db.exists():
            db = AssetDatabase.load_zon(config.db.read_text(encoding="utf-8"))
        else:
            raise SystemExit(1)

    if config.generate:
        generate_files(db)


def generate_files(db: AssetDatabase) -> None:
    for assets in [db.items, db.blocks]:
        for asset in assets.values():
            output = asset.render()
            asset.destination_path.write_text(output, encoding="utf-8")


def parse_args(args: list[str]) -> CliArgs:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo", "-r", type=Path, default=None, help="Path to local Cubyz repo clone."
    )
    parser.add_argument("--db", "-d", type=Path, default=None, help="Path to local asset database.")
    parser.add_argument(
        "--generate",
        "-g",
        action="store_true",
        default=False,
        help="Toggle generation of asset stub markdown files.",
    )
    return CliArgs(**vars(parser.parse_args(args)))


class AssetGenModel(pydantic.BaseModel):
    def dump_zon(
        self, model_dump_params: dict | None = None, zon_params: dict | None = None
    ) -> str:
        model_dump_params = (
            model_dump_params
            if model_dump_params
            else dict(exclude_defaults=True, exclude_none=True)
        )
        model_dict = self.model_dump(**model_dump_params)
        zon_params = zon_params if zon_params else dict(indent="\t")
        return zon.dumps(model_dict, **zon_params)

    @classmethod
    def load_zon(cls, data: str) -> Self:
        """Load a model instance from zon string data."""
        loaded_data = zon.loads(data)
        return cls.model_validate(loaded_data)


class CliArgs(AssetGenModel):
    repo: Path | None = None
    db: Path | None = None
    generate: bool = False


def rebuild_metadata(args: CliArgs) -> AssetDatabase:
    assets = AssetDatabase()
    rebuild_items(args, assets)
    rebuild_blocks(args, assets)
    return assets


def rebuild_items(args: CliArgs, assets: AssetDatabase) -> None:
    assert args.repo is not None
    items_directory = args.repo / Item.ASSET_PATH

    for file_path in items_directory.rglob("**/*.zon", case_sensitive=False):
        if "_migrations" in file_path.name:
            continue

        relative_path = file_path.relative_to(items_directory)
        content = file_path.read_text(encoding="utf-8")
        data = cast(Dict, zon.loads(content))

        id = Id.from_path("cubyz", relative_path)
        assets.items[id] = extract_item(assets, id, data)


def extract_item(assets: AssetDatabase, self_id: Id, data: dict):
    def _get_texture(field: str) -> str | None:
        return data[field] if field in data else None

    return Item(
        tags=tags if (tags := data.get("tags", [])) and isinstance(tags, list) else [],
        material=Material(
            durability=data["material"]["durability"],
            massDamage=data["material"]["massDamage"],
            hardnessDamage=data["material"]["hardnessDamage"],
            swingSpeed=data["material"]["swingSpeed"],
        )
        if "material" in data
        else None,
        texture=_get_texture("texture"),
        self_id=self_id,
        assets_link=assets,
    )


def recursive_update(source: dict, destination: dict):
    # https://stackoverflow.com/a/20666342
    for key, value in source.items():
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            recursive_update(value, node)
        else:
            destination[key] = value

    return destination


def rebuild_blocks(args: CliArgs, assets: AssetDatabase) -> None:
    assert args.repo is not None
    items_directory = args.repo / Block.ASSET_PATH

    defaults = {}

    for file_path in items_directory.rglob("**/*.zon", case_sensitive=False):
        if "_migrations" in file_path.name:
            continue

        if "/textures/" in file_path.as_posix():
            continue

        if "defaults" in file_path.name:
            defaults[file_path.parent.as_posix()] = zon.loads(file_path.read_text(encoding="utf-8"))
            continue

        relative_path = file_path.relative_to(items_directory)
        content = file_path.read_text(encoding="utf-8")
        data = cast(Dict, zon.loads(content))

        base_dict = deepcopy(defaults.get(file_path.parent.as_posix(), {}))
        recursive_update(base_dict, data)

        id = Id.from_path("cubyz", relative_path)

        if "item" in data:
            item = extract_item(assets, id, data["item"])
            assets.items[id] = item

        assets.blocks[id] = extract_block_data(assets, id, data)


def extract_block_data(assets: AssetDatabase, self_id: Id, data: dict) -> Block:
    def _get_texture(field: str) -> str | None:
        if field in data:
            texture_id = data[field]
            _, path = texture_id.split(":", maxsplit=1)
            return path + ".png"
        return None

    return Block(
        tags=tags if (tags := data.get("tags", [])) and isinstance(tags, list) else [],
        block_health=data.get("blockHealth", 1),
        block_resistance=data.get("blockResistance", 0),
        ore=(
            Ore(max_height=ore.get("maxHeight"), min_height=ore.get("minHeight"))
            if (ore := data.get("ore"))
            else None
        ),
        texture=_get_texture("texture"),
        textures=[_get_texture(f"texture{i}") for i in range(16)],
        texture_top=_get_texture("texture_top"),
        texture_bottom=_get_texture("texture_bottom"),
        texture_front=_get_texture("texture_front"),
        texture_left=_get_texture("texture_left"),
        texture_right=_get_texture("texture_right"),
        isInteracive="onInteract" in data,
        self_id=self_id,
        assets_link=assets,
    )


class Id(AssetGenModel):
    model_config = pydantic.ConfigDict(frozen=True)

    addon: str
    path: str

    @classmethod
    def from_str(cls, id: str) -> Self:
        addon, path = id.split(":")
        return cls(addon=addon, path=path)

    @classmethod
    def from_path(cls, addon: str, relative_path: Path) -> Self:
        path = (relative_path.parent / relative_path.name.split(".")[0]).as_posix()
        return cls(addon=addon, path=path)

    @cached_property
    def id(self) -> str:
        return self.addon + ":" + self.path

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, value: object) -> bool:
        return isinstance(value, self.__class__) and self.id == value.id

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return self.id

    @pydantic.model_validator(mode="before")
    @classmethod
    def check_card_number_not_present(cls, data: Any) -> Any:
        if isinstance(data, str):
            addon, path = data.split(":", maxsplit=1)
            return {"addon": addon, "path": path}
        return data

    @pydantic.model_serializer(mode="plain")
    def serialize_model(self) -> str:
        return self.id


class Asset(AssetGenModel):
    TEMPLATE: ClassVar[jinja2.Template]

    self_id: Id = pydantic.Field(exclude=True)
    assets_link: AssetDatabase = pydantic.Field(exclude=True)

    @property
    def id(self) -> str:
        return str(self.self_id)

    @property
    def name(self) -> str:
        return str.join(
            " ", map(str.capitalize, self.file_name.replace("_", " ").replace("-", " ").split(" "))
        )

    @property
    def category(self) -> str:
        return self.__class__.__name__.lower() + "s"

    def render(self) -> str:
        return self.TEMPLATE.render(**{self.__class__.__name__.lower(): self})

    @property
    def file_name(self) -> str:
        return self.self_id.path.replace("/", "_")

    @property
    def destination_path(self) -> Path:
        return DOCS_FOLDER / self.category / f"{self.file_name}.md"

    @property
    def wiki_link(self) -> str:
        return f"/{self.category}/{self.file_name}.html"


class Item(Asset):
    ASSET_PATH: ClassVar[str] = "assets/cubyz/items"
    TEXTURE_PATH: ClassVar[str] = "assets/cubyz/items/textures"
    TEMPLATE: ClassVar[jinja2.Template] = ENV.get_template("item.jinja2.md")

    tags: list[str] = pydantic.Field(default_factory=list)
    material: Material | None = None
    texture: str | None = None
    block_id: Id | None = None

    @property
    def icon(self) -> str:
        return (
            "material/alpha-i-box-outline"
            if self.material is None
            else "material/alpha-m-box-outline"
        )

    @property
    def block(self) -> Block | None:
        return self.assets_link.blocks.get(self.self_id)

    @property
    def image_url(self) -> str:
        if self.texture:
            return f"{CUBYZ_REPO_RAW_CONTENT_BASE_URL}/{self.TEXTURE_PATH}/{self.texture}"
        return "/images/missing.png"


class Material(AssetGenModel):
    durability: float
    massDamage: float
    hardnessDamage: float
    swingSpeed: float


class Block(Asset):
    ASSET_PATH: ClassVar[str] = "assets/cubyz/blocks"
    TEXTURE_PATH: ClassVar[str] = "assets/cubyz/blocks/textures"
    TEMPLATE: ClassVar[jinja2.Template] = ENV.get_template("block.jinja2.md")

    tags: list[str] = pydantic.Field(default_factory=list)
    block_health: float = pydantic.Field(default=1.0)
    block_resistance: float = pydantic.Field(default=0.0)
    ore: Ore | None = None
    texture: str | None = None
    textures: list[str | None] = pydantic.Field(
        default_factory=list, exclude_if=lambda items: not any(items)
    )
    texture_top: str | None = None
    texture_bottom: str | None = None
    texture_front: str | None = None
    texture_left: str | None = None
    texture_right: str | None = None
    isInteracive: bool = False

    @property
    def icon(self) -> str:
        tag_icon_pairs = (
            ("mineable", "material/pickaxe"),
            ("choppable", "material/axe"),
            ("diggable", "material/shovel"),
            ("cuttable", "material/sickle"),
            ("fluid", "material/water"),
        )
        for tag, icon in tag_icon_pairs:
            if tag in self.tags:
                return icon

        return "material/box-shadow"

    @property
    def item(self) -> Item | None:
        return self.assets_link.items.get(self.self_id)

    @property
    def image_url(self) -> str:
        for texture in [
            self.texture,
            self.texture_top,
            *self.textures,
            self.texture_bottom,
            self.texture_front,
            self.texture_left,
            self.texture_right,
        ]:
            if texture:
                return self._image_url(texture)

        return "/images/missing.png"

    def _image_url(self, stem: str) -> str:
        return f"{CUBYZ_REPO_RAW_CONTENT_BASE_URL}/{self.TEXTURE_PATH}/{stem}"


class Ore(AssetGenModel):
    max_height: float | None = None
    min_height: float | None = None


class AssetDatabase(AssetGenModel):
    items: Dict[Id, Item] = pydantic.Field(default_factory=dict)
    blocks: Dict[Id, Block] = pydantic.Field(default_factory=dict)

    @classmethod
    def load_zon(cls, data: str) -> Self:
        raw_data = cast(dict, zon.loads(data))

        self = cls()
        for string_id, raw_obj in raw_data.get("items", {}).items():
            id = Id.from_str(string_id)
            raw_obj.update(
                {
                    "self_id": id,
                    "assets_link": self,
                }
            )

            self.items[id] = Item.model_validate(raw_obj)

        for string_id, raw_obj in raw_data.get("blocks", {}).items():
            id = Id.from_str(string_id)
            raw_obj.update(
                {
                    "self_id": id,
                    "assets_link": self,
                }
            )

            self.blocks[id] = Block.model_validate(raw_obj)

        return self

    def __repr__(self) -> str:
        return "AssetDatabase"


@lru_cache(16)
def load_db_cached(src: str) -> AssetDatabase:
    db = AssetDatabase.load_zon(Path(src).read_text(encoding="utf-8"))
    print(f"Loaded {len(db.items)} items, {len(db.blocks)} blocks")
    return db


if __name__ == "__main__":
    main(sys.argv[1:])
