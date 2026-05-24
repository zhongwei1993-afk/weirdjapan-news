#!/usr/bin/env python3
"""
Inject affiliate IDs into existing Amazon / Booking.com / Klook links across
all blog posts under src/content/blog/.

Usage:
    # 1. Edit the IDS dict below with your real Associates / Awin IDs
    # 2. Dry-run first (no changes written):
    python3 scripts/inject_affiliate_ids.py --dry-run
    # 3. When happy:
    python3 scripts/inject_affiliate_ids.py

The script is idempotent — running it twice does NOT double-tag URLs.
It rewrites raw URLs in markdown into their tagged equivalents.

Supported partners:
- Amazon US/JP: appends ?tag=<id> (or &tag=<id> if URL already has params)
- Booking.com:  appends ?aid=<id>&label=<label> (Awin / direct affiliate IDs)
- Klook:        appends ?aid=<id> (Awin or direct Klook Affiliate ID)
"""

import argparse
import re
import sys
import urllib.parse
from pathlib import Path

# ===========================================================================
# EDIT THESE WITH YOUR REAL IDS BEFORE RUNNING (without --dry-run)
# ===========================================================================
IDS = {
    "amazon_us_tag": "weirdjapan-20",   # replace with real Associates ID
    "amazon_jp_tag": "weirdjapan-22",   # replace with real Associates ID
    "booking_aid": "0000000",            # replace with Awin or Booking affiliate aid
    "booking_label": "weirdjapan",
    "klook_aid": "000000",               # replace with Awin or Klook affiliate aid
}
# ===========================================================================

BLOG_DIR = Path(__file__).resolve().parent.parent / "src" / "content" / "blog"


def tag_url(url: str, params_to_add: dict) -> str:
    """Add query params to URL idempotently (skip if any of the keys already exist)."""
    parsed = urllib.parse.urlparse(url)
    existing = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
    # If any of the target keys are already present, leave the URL alone
    if any(key in existing for key in params_to_add):
        return url
    existing.update({k: [v] for k, v in params_to_add.items()})
    new_query = urllib.parse.urlencode(
        [(k, v) for k, vs in existing.items() for v in vs]
    )
    return urllib.parse.urlunparse(parsed._replace(query=new_query))


def rewrite_amazon(url: str) -> str:
    """Append ?tag=<amazon_us_tag>. OneLink handles JP redirect server-side."""
    # Only touch amazon.com and amazon.co.jp domains
    if "amazon.com" in url:
        return tag_url(url, {"tag": IDS["amazon_us_tag"]})
    if "amazon.co.jp" in url:
        return tag_url(url, {"tag": IDS["amazon_jp_tag"]})
    return url


def rewrite_booking(url: str) -> str:
    return tag_url(
        url,
        {"aid": IDS["booking_aid"], "label": IDS["booking_label"]},
    )


def rewrite_klook(url: str) -> str:
    return tag_url(url, {"aid": IDS["klook_aid"]})


# Match raw URLs inside markdown — both [text](url) and bare. We're conservative
# and only match within a () group (markdown link target) to avoid touching
# code blocks accidentally.
URL_IN_LINK_RE = re.compile(r"\((https?://[^\s)]+)\)")


def process_file(path: Path, dry_run: bool = False) -> int:
    """Rewrite URLs in a single markdown file. Returns count of URLs changed."""
    original = path.read_text(encoding="utf-8")
    changes = 0

    def replace(match: re.Match) -> str:
        nonlocal changes
        url = match.group(1)
        if "amazon.com" in url or "amazon.co.jp" in url:
            new = rewrite_amazon(url)
        elif "booking.com" in url:
            new = rewrite_booking(url)
        elif "klook.com" in url:
            new = rewrite_klook(url)
        else:
            return match.group(0)
        if new != url:
            changes += 1
        return f"({new})"

    rewritten = URL_IN_LINK_RE.sub(replace, original)
    if changes and not dry_run:
        path.write_text(rewritten, encoding="utf-8")
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change but don't write files",
    )
    args = parser.parse_args()

    # Sanity check: refuse to write placeholder IDs
    if not args.dry_run:
        placeholders = ["weirdjapan-20", "weirdjapan-22", "0000000", "000000"]
        if any(v in placeholders for v in IDS.values()):
            print(
                "ERROR: Placeholder IDs still in script. Edit IDS{} dict with "
                "real IDs from your ASP dashboards, or run with --dry-run.",
                file=sys.stderr,
            )
            return 2

    total_changes = 0
    total_files = 0
    for md in sorted(BLOG_DIR.glob("*.md")):
        n = process_file(md, dry_run=args.dry_run)
        if n:
            print(f"{md.name}: {n} link{'s' if n != 1 else ''}")
            total_files += 1
            total_changes += n

    verb = "would change" if args.dry_run else "changed"
    print(f"\n{verb} {total_changes} URLs across {total_files} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
