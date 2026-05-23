#!/usr/bin/env python3
"""Fetch one Wikimedia Commons image per keyword via API (no auth needed)."""
import json
import os
import ssl
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(__file__)
KEYWORDS_PATH = os.path.join(HERE, "keywords.json")
OUT_PATH = os.path.join(HERE, "image_urls_wm.json")

UA = "WeirdJapanBot/1.0 (https://weirdjapan.news; admin@weirdjapan.news)"

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE


def fetch_one(slug_keyword):
    slug, keyword = slug_keyword
    query = urllib.parse.quote(keyword)
    api_url = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&format=json&list=search&srsearch={query}&srnamespace=6&srlimit=5"
    )
    req = urllib.request.Request(api_url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        return slug, None, str(e)

    hits = data.get("query", {}).get("search", [])
    if not hits:
        return slug, None, "no results"

    # Take first image file, prefer jpg/jpeg/png (not svg/gif/pdf)
    for hit in hits:
        title = hit.get("title", "")
        if title.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            filename = title.replace("File:", "")
            # Special:FilePath redirects to actual image
            image_url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{urllib.parse.quote(filename)}?width=1600"
            return slug, {"url": image_url, "filename": filename, "title": title}, None

    return slug, None, "no jpg/png in top 5"


def main():
    with open(KEYWORDS_PATH) as f:
        keywords = json.load(f)

    existing = {}
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH) as f:
            existing = json.load(f)

    todo = [(slug, kw) for slug, kw in keywords.items() if slug not in existing or not existing.get(slug)]
    print(f"📋 既存: {len(existing)}件 / 取得対象: {len(todo)}件 / 合計: {len(keywords)}件")

    results = dict(existing)
    failed = []

    with ThreadPoolExecutor(max_workers=15) as ex:
        for slug, info, err in ex.map(fetch_one, todo):
            if info:
                results[slug] = info
                print(f"  ✅ {slug}: {info['filename'][:50]}")
            else:
                failed.append((slug, err))
                print(f"  ⚠️ {slug}: {err}")

    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n📊 取得成功: {len(results)} / {len(keywords)}")
    if failed:
        print(f"❌ 失敗: {len(failed)}")
    print(f"💾 {OUT_PATH}")


if __name__ == "__main__":
    main()
