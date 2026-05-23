#!/usr/bin/env python3
"""Retry missing 9 items with alternate keywords."""
import json, os, ssl, urllib.request, urllib.parse

HERE = os.path.dirname(__file__)
OUT_PATH = os.path.join(HERE, "image_urls_wm.json")

UA = "WeirdJapanBot/1.0 (https://weirdjapan.news; admin@weirdjapan.news)"
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

ALT = {
    "nap-cafes-tokyo": "Sleeping man Japan",
    "alien-restaurant-tokyo": "Robot restaurant Shinjuku",
    "butler-cafe-shibuya": "Butler costume",
    "fruit-bus-stops-nagasaki": "Konagai bus stop",
    "earthquake-warning-system": "Japan earthquake aftermath",
    "omurice-history": "Omelette rice",
    "kakigori-cloud-ice": "Shaved ice dessert",
    "hikikomori-1-5-million": "Empty bedroom",
    "inemuri-meeting-naps": "Sleeping at desk Japan",
}


def fetch_one(keyword):
    query = urllib.parse.quote(keyword)
    api_url = (
        f"https://commons.wikimedia.org/w/api.php?"
        f"action=query&format=json&list=search&srsearch={query}&srnamespace=6&srlimit=10"
    )
    req = urllib.request.Request(api_url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    for hit in data.get("query", {}).get("search", []):
        title = hit.get("title", "")
        if title.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            filename = title.replace("File:", "")
            return {
                "url": f"https://commons.wikimedia.org/wiki/Special:FilePath/{urllib.parse.quote(filename)}?width=1600",
                "filename": filename,
                "title": title,
            }
    return None


def main():
    with open(OUT_PATH) as f:
        data = json.load(f)

    for slug, kw in ALT.items():
        try:
            info = fetch_one(kw)
            if info:
                data[slug] = info
                print(f"✅ {slug}: {info['filename'][:60]}")
            else:
                print(f"⚠️ {slug}: no jpg in {kw}")
        except Exception as e:
            print(f"❌ {slug}: {e}")

    with open(OUT_PATH, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n📊 合計: {len(data)}/100")


if __name__ == "__main__":
    main()
