# カタカナ Flashcards

A self-contained browser flashcard app for practising the 227 most common katakana loanwords. No server, no dependencies — just open `index.html`.

## How it works

Each card shows a katakana word (e.g. **タクシー**). Switch your IME to katakana mode and type the word back, then press **Check** (or Enter). The app immediately shows:

- ✓ / ✗ verdict
- The English meaning
- The romaji reading

Press **Next** (or Enter) to continue.

## Spaced repetition (SM-2)

Card scheduling uses the [SM-2](https://www.supermemo.com/en/blog/application-of-a-computer-to-improve-the-results-obtained-in-working-with-the-supermemo-method) algorithm:

| Result | Effect |
|--------|--------|
| Correct | Interval grows: 1 day → 6 days → ×ease-factor |
| Incorrect | Card resets to 1-day interval and is re-queued in the current session |

Progress is stored in `localStorage` — it persists across page reloads in the same browser.

Each session loads all overdue reviews first, then up to **20 new cards**. Once a session is complete you can immediately start more new cards if any remain unseen.

## Word list

227 unique words extracted from a curated list of the most-used katakana vocabulary. The order is randomised on each page load so different users (or sessions) see cards in a different sequence.

The source data lives in [`katakana_words.csv`](katakana_words.csv) with columns: `Katakana`, `Romaji`, `Meaning`.

## Usage

### Open locally
```
open index.html
```
`localStorage` works fine with `file://` URLs, so progress is saved.

### Serve locally (optional)
```bash
python3 -m http.server
# open http://localhost:8000
```

### Deploy
The app is a single static file — any static host works:

- **GitHub Pages** — enable Pages in repo Settings, point to `main` branch root
- **Netlify Drop** — drag the project folder onto [netlify.com/drop](https://app.netlify.com/drop)
- **Vercel** — `npx vercel` in the project directory

## iOS notes

- Use the **Check** button to submit answers — the iOS virtual keyboard does not reliably fire Enter key events.
- Switch your keyboard to **カタカナ** mode before typing (Japanese keyboard → hold あ/ka key → select カタカナ).

## Files

| File | Description |
|------|-------------|
| `index.html` | The entire app — HTML, CSS, JS, and word data |
| `katakana_words.csv` | Source word list (Katakana, Romaji, Meaning) |
| `example_katakana_list.html` | Original scraped source page |
| `main.py` | Python helper used to extract and deduplicate the CSV |
