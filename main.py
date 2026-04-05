import argparse
import csv
import json
import re

SMALL_KANA = set("ァィゥェォャュョッヮヵヶ")
KATAKANA_RE = re.compile(r"^[\u30A0-\u30FF]+$")


def is_valid_katakana_word(word: str) -> bool:
    """Return True if the word passes all quality filters."""
    # Must be pure katakana (no kanji, hiragana, punctuation etc.)
    if not KATAKANA_RE.match(word):
        return False
    # Single character — not a useful flashcard
    if len(word) < 2:
        return False
    # Contains ・ — compound / multi-word entry
    if "・" in word:
        return False
    # Two or more consecutive ー — expressive elongation (e.g. キタァー)
    if re.search(r"ー{2,}", word):
        return False
    # Any character repeated 3+ times — expressive noise (e.g. ァァァアア)
    if re.search(r"(.)\1{2,}", word):
        return False
    # Very long strings (≥10 chars) — usually concatenated product names
    if len(word) >= 10:
        return False
    # Starts with a small kana — always a fragment, never a real word
    if word[0] in SMALL_KANA:
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Build index.html from a CSV word list.")
    parser.add_argument("csv", help="CSV file with columns: rank,word,romaji,frequency,english")
    parser.add_argument("-n", "--limit", type=int, default=None, help="Maximum number of words to include")
    args = parser.parse_args()

    with open(args.csv, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if args.limit is not None:
        rows = rows[:args.limit]

    entries = [
        [row["word"], row["romaji"], row["english"]]
        for row in rows
    ]
    words_js = json.dumps(entries, ensure_ascii=False, separators=(",", ":"))[1:-1]

    with open("index.template.html", encoding="utf-8") as f:
        template = f.read()

    output = template.replace("{{WORDS}}", words_js)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Built index.html with {len(entries)} words.")


if __name__ == "__main__":
    main()
