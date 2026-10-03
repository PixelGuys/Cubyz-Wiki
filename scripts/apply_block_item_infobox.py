from __future__ import annotations

import re
import sys
from pathlib import Path

THIS_DIRECTORY = Path(__file__).parent.resolve()
REPO_ROOT = THIS_DIRECTORY.parent
sys.path.append(REPO_ROOT.as_posix())

from scripts.assetgen2 import AssetDatabase, Id

DOCS = REPO_ROOT / "docs"

REDIRECT = re.compile(
    r"\n*<script>\s*\n\s*window\.location\.replace\([^)]*\);\s*\n</script>\n*",
    re.DOTALL,
)
ITEM_INFOBOX = re.compile(
    r'!!! infobox "([^"]+)"\n\n\{\{ block_infobox\("([^"]+)"\) \}\}'
)


def main() -> None:
    db = AssetDatabase.load_zon((THIS_DIRECTORY / "assets.zon").read_text(encoding="utf-8"))

    updated = 0
    for page in sorted((DOCS / "blocks").rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        if "window.location.replace" not in text:
            continue

        match = ITEM_INFOBOX.search(text)
        if not match:
            print(f"  no block infobox, skipped: {page.relative_to(REPO_ROOT)}")
            continue

        block_id = match.group(2)
        id = Id.from_str(block_id)
        item = db.items.get(id)
        if item is None:
            print(f"  no item for {block_id}, skipped: {page.relative_to(REPO_ROOT)}")
            continue

        # Insert the item infobox before the block infobox.
        item_box = (
            f'!!! infobox "{item.name} (item)"\n\n'
            f'{{{{ item_infobox("{item.id}") }}}}\n\n'
        )
        text = text[: match.start()] + item_box + text[match.start() :]
        # Remove the redirect script.
        text = REDIRECT.sub("\n\n", text, count=1)
        # Tidy up excess blank lines left behind.
        text = re.sub(r"\n{4,}", "\n\n\n", text)

        page.write_text(text, encoding="utf-8")
        updated += 1

    print(f"Updated {updated} block pages")


if __name__ == "__main__":
    main()
