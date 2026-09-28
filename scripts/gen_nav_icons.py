from __future__ import annotations

import sys
from pathlib import Path

THIS_DIRECTORY = Path(__file__).parent.resolve()
REPO_ROOT = THIS_DIRECTORY.parent
sys.path.append(REPO_ROOT.as_posix())

from scripts.assetgen2 import AssetDatabase, Block, Id, CUBYZ_REPO_RAW_CONTENT_BASE_URL

ICONS_DIR = REPO_ROOT / "theme" / "overrides" / ".icons" / "wiki"

SVG_TEMPLATE = (
    '<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
    'viewBox="0 0 24 24" width="24" height="24">'
    '<image href="{url}" xlink:href="{url}" x="3" y="3" width="18" height="18" '
    'preserveAspectRatio="xMidYMid meet" image-rendering="pixelated"/>'
    "</svg>"
)


def texture_url(item_or_block) -> str | None:
    for attr in ("texture", "texture_top", "texture_bottom", "texture_front", "texture_left", "texture_right"):
        value = getattr(item_or_block, attr, None)
        if value:
            return item_or_block._image_url(value) if hasattr(item_or_block, "_image_url") else (
                f"{CUBYZ_REPO_RAW_CONTENT_BASE_URL}/{item_or_block.TEXTURE_PATH}/{value}"
            )
    for value in getattr(item_or_block, "textures", []) or []:
        if value:
            return item_or_block._image_url(value)
    return None


def main() -> None:
    db = AssetDatabase.load_zon((THIS_DIRECTORY / "assets.zon").read_text(encoding="utf-8"))
    ICONS_DIR.mkdir(parents=True, exist_ok=True)

    for stale in ICONS_DIR.glob("*.svg"):
        stale.unlink()

    written = 0
    for assets in (db.blocks, db.items):
        for id, asset in assets.items():
            # Blocks without an item (e.g. log orientation variants) don't get a page or icon.
            if isinstance(asset, Block) and not asset.has_item:
                continue

            url = texture_url(asset)
            if not url:
                continue
            name = id.path.replace("/", "-")
            (ICONS_DIR / f"{name}.svg").write_text(SVG_TEMPLATE.format(url=url), encoding="utf-8")
            written += 1

    print(f"Wrote {written} nav icon SVGs to {ICONS_DIR.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
