from __future__ import annotations

import sys
from pathlib import Path

THIS_DIRECTORY = Path(__file__).parent.resolve()
REPO_ROOT = THIS_DIRECTORY.parent
sys.path.append(REPO_ROOT.as_posix())

from scripts.assetgen2 import AssetDatabase, Id

DOCS = REPO_ROOT / "docs"


def title(name: str) -> str:
    return name.replace("_", " ").replace("-", " ").title()


def existing_recipe_paths(db: AssetDatabase) -> list[tuple[str, str]]:
    """Return (page_dir, icon_key) for every generated asset page."""
    entries: list[tuple[str, str]] = []
    for assets in (db.blocks, db.items):
        for id, asset in assets.items():
            icon_key = id.path.replace("/", "-")
            page_dir = asset.path_no_extension[len(asset.category) + 1 :]
            entries.append((page_dir, icon_key))
    return entries


def main() -> None:
    db = AssetDatabase.load_zon((THIS_DIRECTORY / "assets.zon").read_text(encoding="utf-8"))
    pages = existing_recipe_paths(db)

    icons_dir = REPO_ROOT / "theme" / "overrides" / ".icons" / "wiki"

    created = 0
    for area in ("items", "blocks"):
        for category_dir in sorted((DOCS / area).rglob("*")):
            if not category_dir.is_dir():
                continue
            index = category_dir / "index.md"
            if index.exists():
                continue

            # Find an icon-bearing child asset page in this directory.
            prefix = category_dir.relative_to(DOCS / area).as_posix()
            child_icons = sorted(
                icon_key
                for page_dir, icon_key in pages
                if page_dir.rsplit("/", maxsplit=1)[0] == prefix
                and (icons_dir / f"{icon_key}.svg").is_file()
            )
            if not child_icons:
                continue

            name = title(category_dir.name)
            index.write_text(
                f"---\nicon: wiki/{child_icons[0]}\n---\n\n# {name}\n",
                encoding="utf-8",
            )
            created += 1

    print(f"Created {created} category index pages")


if __name__ == "__main__":
    main()
