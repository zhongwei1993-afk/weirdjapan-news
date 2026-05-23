#!/usr/bin/env python3
"""Fetch one Unsplash photo ID per keyword via concurrent HTTP requests."""
import json
import re
import os
import ssl
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import urllib.parse

# Bypass SSL verification (we're just scraping public image URLs)
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

HERE = os.path.dirname(__file__)
KEYWORDS_PATH = os.path.join(HERE, "keywords.json")
OUT_PATH = os.path.join(HERE, "image_urls.json")

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# Pattern matches photo IDs but NOT premium_photo
PHOTO_RE = re.compile(r'https://images\.unsplash\.com/(photo-[a-f0-9-]+)\?')


def fetch_one(slug_keyword):
    slug, keyword = slug_keyword
    query = urllib.parse.quote(keyword)
    url = f"https://unsplash.com/s/photos/{query}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return slug, None, str(e)

    # Get unique photo IDs in order of appearance, skip the first few (often layout) and take a stable one
    seen = []
    for m in PHOTO_RE.finditer(html):
        pid = m.group(1)
        if pid not in seen:
            seen.append(pid)
        if len(seen) >= 8:
            break
    if not seen:
        return slug, None, "no photo found"
    # Pick the 1st (top result)
    return slug, seen[0], None


def main():
    with open(KEYWORDS_PATH) as f:
        keywords = json.load(f)

    # Load existing results
    existing = {}
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH) as f:
            existing = json.load(f)

    todo = [(slug, kw) for slug, kw in keywords.items() if slug not in existing or not existing.get(slug)]
    print(f"📋 既存: {len(existing)}件 / 取得対象: {len(todo)}件 / 合計: {len(keywords)}件")

    results = dict(existing)
    failed = []

    with ThreadPoolExecutor(max_workers=20) as ex:
        for slug, pid, err in ex.map(fetch_one, todo):
            if pid:
                results[slug] = pid
                print(f"  ✅ {slug}: {pid}")
            else:
                failed.append((slug, err))
                print(f"  ⚠️ {slug}: {err}")

    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n📊 取得成功: {len(results)} / {len(keywords)}")
    if failed:
        print(f"❌ 失敗: {len(failed)}")
        for slug, err in failed:
            print(f"   {slug}: {err}")
    print(f"💾 {OUT_PATH}")


if __name__ == "__main__":
    main()
