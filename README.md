# カタカナ Flashcards

A self-contained browser flashcard app for practising katakana loanwords. No server required — just open `index.html`.

## How it works

Each card shows a katakana word (e.g. **タクシー**). Type the word back in katakana and press **Check** (or Enter). The app shows:

- ✓ / ✗ verdict
- The English meaning (or a Google search link if the word has no known translation)
- The romaji reading

Press **Next** (or Enter) to continue.

Input accepts katakana directly, or romaji converted on-the-fly via [wanakana](https://github.com/WaniKani/WanaKana) (e.g. type `ta-ku-shi-` → `タクシー`).

## Scheduling

Card scheduling uses a probability-based spaced repetition system (session-scoped, no persistence):

- Incorrect cards resurface almost immediately
- Correct cards are deprioritised
- All words stay in the pool for the duration of the session

## Word list

`index.html` is generated from a CSV word list using `main.py`. The word list (`words/katakana_annotated-new.csv`) was derived from the [JPN News 2023 30K frequency list](words/jpn_news_2023_30K-words.txt) by:

1. Extracting all pure-katakana words
2. Filtering noise (compounds, single chars, repeated characters, fragments, very long strings)
3. Annotating with English meanings via [JMdict](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) (using `jamdict`)
4. Adding romaji via `pykakasi` (Hepburn with macrons)

## Building index.html

Requires [uv](https://docs.astral.sh/uv/).

```bash
# Full word list (~6900 words)
uv run python3 main.py words/katakana_annotated-new.csv

# Limit to the N most frequent words
uv run python3 main.py words/katakana_annotated-new.csv -n 500
```

## Usage

### Open locally
```
open index.html
```

### Deploy
The app is a single static file — any static host works:

- **GitHub Pages** — enable Pages in repo Settings, point to `main` branch root
- **Netlify Drop** — drag the project folder onto [netlify.com/drop](https://app.netlify.com/drop)

## iOS notes

- Use the **Check** button to submit — the iOS virtual keyboard does not reliably fire Enter.
- Switch to **カタカナ** input mode before typing (Japanese keyboard → hold あ → select カタカナ).

## Files

| File | Description |
|------|-------------|
| `index.html` | The built app — HTML, CSS, JS, and word data |
| `index.template.html` | Template with `{{WORDS}}` placeholder |
| `main.py` | Build script: renders template from a CSV, with `is_valid_katakana_word()` filter function |
| `words/jpn_news_2023_30K-words.txt` | Source frequency list (Japanese News 2023) |
| `words/katakana_only.csv` | Filtered katakana-only words (rank, word, frequency) |
| `words/katakana_annotated-new.csv` | Final word list with romaji and English meanings |
| `words/katakana_words.csv` | Original hand-curated word list |
