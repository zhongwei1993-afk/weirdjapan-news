# Affiliate ASP 申請ガイド (ボス向け)

`/disclosure` ページと Footer の Amazon 必須文言の整備は完了 (デプロイ後反映)。以下、4つのASPへの申請手順。**並行で申請するのが最速** — 承認に1-7日かかるため、待ち時間を重ねないこと。

すべて取得したら、Chief が `scripts/inject_affiliate_ids.py` で65リンクに一括埋め込み + push します。

---

## 1. Amazon Associates US — 最優先 (即日承認多い)

**サイト**: https://affiliate-program.amazon.com/
**所要時間**: アカウント登録 ~10分、即日〜3日で承認
**必要書類**:
- 米国住所 (なくてもOK、日本住所で申請可。Tax は W-8BEN を提出)
- 銀行口座 (日本の銀行可。USドル口座 or `Send a check` 受取)
- サイトURL: `https://weirdjapan.news`
- サイトのトラフィック源説明 (Organic / Direct で OK)

**申請フォームの「How do you drive traffic to your site?」の回答例 (英語)**:
> WeirdJapan.news is an English-language editorial blog about Japanese culture
> oddities, food, and travel. We have 100+ long-form articles (1,200-1,600
> words each) covering Tokyo travel guides, food culture, and lifestyle. Traffic
> sources are: organic search (target: US/UK/CA/AU travelers researching Japan
> trips), direct readers (newsletter, social), and Reddit/Pinterest referrals.
> We participate in affiliate programs to fund editorial costs without
> sacrificing editorial independence. Our affiliate disclosure is publicly posted
> at https://weirdjapan.news/disclosure.

**Associates ID**: 申請時に好きなIDを設定可 (例: `weirdjapan-20` ← 推奨)。これが `?tag=weirdjapan-20` として全リンクに入る。

**承認後**: Associates ID を Chief に教えるだけで、65リンクに一括埋め込みします。

---

## 2. Amazon Associates JP

**サイト**: https://affiliate.amazon.co.jp/
**所要時間**: アカウント登録 ~10分、3日以内で承認
**必要書類**:
- 日本住所、日本の銀行口座
- マイナンバー (税務処理用)
- サイトURL: `https://weirdjapan.news`

**Associates ID**: 例 `weirdjapan-22` (jp版は `-22` サフィックス慣例)

**OneLink設定**:
1. 米国Associatesアカウントにログイン
2. Tools → OneLink → "Set up your OneLink"
3. 「米国 → JP は `weirdjapan-22` へ転送」と設定
4. これで weirdjapan-20 リンクを貼っておけば、JP読者は自動的に Amazon.co.jp に転送 + JP commission

---

## 3. Awin (Booking.com + Klook 含む 12+ 大手一括)

**サイト**: https://www.awin.com/gb/publishers
**所要時間**: 申請 ~20分、$5 審査料 (承認後返金されるrebate)、3-5営業日で承認
**必要書類**:
- パスポートまたは身分証
- 銀行口座 (日本可、月次振込 minimum £20)
- サイトURL + トラフィックデータ (GAスクショ歓迎)

**申請文 (英語) **:
> WeirdJapan.news is an English-language editorial blog covering Japanese
> culture, travel, and food. We publish 1,200-1,600 word long-form articles,
> currently 100+ posts indexed. Target audience: US/UK/CA/AU travelers planning
> Japan trips. We currently link to Booking.com (18 articles), Klook (31
> articles), and Amazon (14 articles) editorially — joining Awin lets us
> properly attribute referrals across these partners. Disclosure:
> https://weirdjapan.news/disclosure.

**承認後の追加申請**:
Awin内で個別マーチャント (Booking.com, Klook, GetYourGuide, Viator, Agoda等) に追加申請する。Booking.com は別途 ~1-3日。Klook は通常即時。

---

## 4. A8.net + もしもアフィリエイト (日本ASP)

### A8.net
**サイト**: https://www.a8.net/as/as_join/registration.html
**所要時間**: 即時登録、即時承認 (審査なし)
**必要書類**: 日本住所、日本銀行口座、サイトURL
**カバー**: 楽天トラベル、Booking.com (日本支店)、JR東日本、その他日本系

### もしもアフィリエイト
**サイト**: https://af.moshimo.com/
**所要時間**: 即時登録、サイト審査 ~3日
**必要書類**: 同上
**特徴**: **「もしも経由でAmazonリンクを貼ると、Amazon Associates の通常 commission に上乗せで「W報酬」** (1-10%追加)。Amazon ID取得後は、もしも経由のリンクに切り替えると収益アップ

---

## 申請順序の推奨

並行で動かす場合、午後の30分で全部行ける:

1. **Amazon US** (10分) ← 最重要、即日〜3日承認
2. **Amazon JP** (10分) ← Amazon USとほぼ同時
3. **Awin** (20分) ← $5審査料、3-5営業日
4. **A8.net** (5分) ← 即時承認
5. **もしも** (10分) ← 3日審査

**Total ボス側所要**: 約 1時間 (フォーム入力のみ)。あとは承認待ち。

---

## 承認後、Chief 側の作業

ボスから以下のIDを共有してもらえば、Chief が即座に全65リンクに一括埋め込み + push します:

```
Amazon US Associates ID:     weirdjapan-20 (例)
Amazon JP Associates ID:     weirdjapan-22 (例)
Awin Publisher ID:           XXXXXX
Booking.com Affiliate ID:    YYYYYY (Awin経由) または aid=ZZZZ&label=WJ
Klook Affiliate ID:          AAA-BBB (Awin経由 または 直契約)
A8.net サイトID:             XXXX-XXXX
もしも メディアID:            XXXXXXXX
```

埋め込みは `scripts/inject_affiliate_ids.py` (準備完了) で自動化されます。

---

## 各ASPの記事内表記ルール (収益最大化)

承認後、新規記事は以下の指針で:

- **Amazon**: 「[商品名 on Amazon](amazon link)」CTA推奨 (商品名+Amazon併記が CTR高)
- **Booking.com**: 「Check rates on Booking.com」CTA、星評価・価格帯併記
- **Klook**: 「Book on Klook (with English support)」CTA、料金併記
- 各記事の3-5箇所に分散配置 (本文中段 + 末尾CTA)
- 1記事に1ASPだけでなく、Hotel = Booking + Tour = Klook の組合せ推奨

---

## 質問・トラブル対応

申請でハマったら Chief に相談してください。各ASPのよくある rejection 理由 (サイトコンテンツ薄い、disclosure不十分、トラフィック説明曖昧等) は事前に対策済みです。
