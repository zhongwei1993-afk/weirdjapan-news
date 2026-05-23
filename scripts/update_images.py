#!/usr/bin/env python3
"""Replace heroImage* frontmatter in 100 article markdown files with unique Wikimedia images."""
import json, os, re, urllib.parse

HERE = os.path.dirname(__file__)
BLOG_DIR = os.path.join(HERE, "..", "src", "content", "blog")
IMG_JSON = os.path.join(HERE, "image_urls_wm.json")

with open(IMG_JSON) as f:
    images = json.load(f)


def make_alt(filename):
    # "Tokyo_Skyline_2023.jpg" → "Tokyo Skyline 2023"
    name = re.sub(r'\.(jpg|jpeg|png|webp)$', '', filename, flags=re.I)
    name = name.replace('_', ' ').replace('-', ' ')
    # Remove all double quotes to keep YAML safe
    name = name.replace('"', '').replace("'", '')
    return name[:200].strip()


updated = 0
skipped = 0

for slug, info in images.items():
    path = os.path.join(BLOG_DIR, f"{slug}.md")
    if not os.path.exists(path):
        print(f"⚠️ ファイル無し: {slug}.md")
        skipped += 1
        continue

    with open(path) as f:
        content = f.read()

    url = info["url"]
    alt = make_alt(info["filename"])
    title_quoted = urllib.parse.quote(info["title"].replace(' ', '_'))
    credit_url = f"https://commons.wikimedia.org/wiki/{title_quoted}"
    credit = "Image via Wikimedia Commons"

    # Replace each frontmatter line (whole line based)
    content = re.sub(r'^heroImageUrl:.*$', f'heroImageUrl: "{url}"', content, count=1, flags=re.MULTILINE)
    content = re.sub(r'^heroImageAlt:.*$', f'heroImageAlt: "{alt}"', content, count=1, flags=re.MULTILINE)
    content = re.sub(r'^heroImageCredit:.*$', f'heroImageCredit: "{credit}"', content, count=1, flags=re.MULTILINE)
    content = re.sub(r'^heroImageCreditUrl:.*$', f'heroImageCreditUrl: "{credit_url}"', content, count=1, flags=re.MULTILINE)

    with open(path, "w") as f:
        f.write(content)
    updated += 1

print(f"✅ 更新: {updated} / スキップ: {skipped}")
