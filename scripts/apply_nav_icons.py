from __future__ import annotations

import re
import sys
from pathlib import Path

THIS_DIRECTORY = Path(__file__).parent.resolve()
REPO_ROOT = THIS_DIRECTORY.parent
sys.path.append(REPO_ROOT.as_posix())

from scripts.assetgen2 import AssetDatabase, Id

DOCS = REPO_ROOT / "docs"
ICONS_DIR = REPO_ROOT / "theme" / "overrides" / ".icons" / "wiki"

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
ICON_LINE = re.compile(r"^icon:.*$", re.MULTILINE)


def page_to_icon_key(db: AssetDatabase) -> dict[str, str]:
    """Map each generated page path (relative to items/blocks) to its icon key."""
    mapping: dict[str, str] = {}
    for assets in (db.blocks, db.items):
        for id, asset in assets.items():
            icon_key = id.path.replace("/", "-")
            if not (ICONS_DIR / f"{icon_key}.svg").is_file():
                continue
            mapping[asset.path_no_extension[len(asset.category) + 1 :]] = icon_key
    return mapping


def main() -> None:
    db = AssetDatabase.load_zon((THIS_DIRECTORY / "assets.zon").read_text(encoding="utf-8"))
    known = page_to_icon_key(db)

    updated = 0
    skipped: list[str] = []
    for area in ("items", "blocks"):
        for page in sorted((DOCS / area).rglob("*.md")):
            name = page.relative_to(DOCS / area).with_suffix("").as_posix()
            if name not in known:
                skipped.append(f"{area}/{name}")
                continue

            icon_key = known[name]

            text = page.read_text(encoding="utf-8")
            match = FRONT_MATTER.match(text)
            if not match:
                skipped.append(f"{area}/{name} (no front matter)")
                continue

            new_line = f"icon: wiki/{icon_key}"
            body = match.group(1)
            if ICON_LINE.search(body):
                new_body = ICON_LINE.sub(new_line, body, count=1)
            else:
                new_body = body + "\n" + new_line
            new_text = text[: match.start(1)] + new_body + text[match.end(1) :]

            if new_text != text:
                page.write_text(new_text, encoding="utf-8")
                updated += 1

    print(f"Updated {updated} pages; skipped {len(skipped)}")
    for item in skipped:
        print(f"  skipped: {item}")


if __name__ == "__main__":
    main()
