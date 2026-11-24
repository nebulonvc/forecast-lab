# Audit: txt-00013 quote restored (do not bypass year-screen)

Time: 2026-11-16 15:07 Asia/Shanghai
Worker: bot2-w23
Case: oecd-governing-with-ai-v5
Item: the sole candidate in txt-00013 (answers.jsonl). This is an adjustment of an already-extracted item; previous version retained below.

## Why the previous quote was wrong
The first persisted quote omitted `OECD (2024[24])` so that `mentioned_years` would not be {2024} and `rule_quote` would not return `historical` (because `publication_year_proxy=2025` and English “the next 10 years” does not match Chinese `_FUTURE_WINDOW`). That trim was a pipeline workaround. It hid the cited research’s date, which is the actual anchor of “the next 10 years,” and it weakened attribution (this 2025 report is restating OECD 2024 research, not issuing a new 10-year window from 18 September 2025).

## Source context (verbatim)
Although some AI experts predict significant economic gains from AI, OECD (2024[24]) research indicates
more tepid growth, estimating annual productivity growth due to AI ranging between 0.25-0.6 percentage
points over the next 10 years in the most AI-ready countries.

Chapter 1 References identify [24] as:
Filippucci, F., P. Gal and M. Schief (2024), “Miracle or Myth? Assessing the macroeconomic
productivity gains from Artificial Intelligence”, OECD Artificial Intelligence Papers, No. 29,
OECD Publishing, Paris, https://doi.org/10.1787/b524a072-en.

Independent bibliographic record: OECD page date 22 November 2024. The 2024 paper itself frames the estimate as macroeconomic productivity gains “over a 10-year horizon” / “over the next 10 years,” with main scenarios of 0.25–0.6 percentage points annual TFP growth in the United States (labour productivity 0.4–0.9 pp.), and other economies of similar magnitude but somewhat lower. The 2025 book’s wording “in the most AI-ready countries” is the book’s paraphrase of that research.

## Horizon and attribution decision (not fabricated)
- Horizon wording in the book: “the next 10 years” (verbatim; same-line changes: “points over the next 10 years”).
- Window start: the cited OECD (2024[24]) paper’s horizon, approximately from late 2024 into the mid-2030s — **not** a new window starting at this report’s publication date 2025-09-18.
- Attribution: `author_endorsed`, speaker OECD. The 2025 report says “OECD (2024[24]) research indicates …,” presenting the Organisation’s own 2024 finding as the contrast to “some AI experts.” Not recoded as `reported` to change scoring, and not recoded as a fresh 2025 author forecast.
- The estimate is still only partly elapsed at cutoff 2026-11-15.

## Pipeline year-screen (expected false historical)
`rule_quote`: if `publication_year` is set and `mentioned_years` are non-empty and `max(years) < publication_year` and `_FUTURE_WINDOW` does not match, return `historical`.
- `_YEAR` will capture 2024 from “OECD (2024[24])”.
- `_FUTURE_WINDOW` is Chinese only (`明年|后年|今后|未来|…|\d+\s*年内|到 20xx|20xx 年 前/后/内…`) and does not match English “the next 10 years”.
- Therefore `claims_from_results` will likely **exclude** the item as `historical` (METHOD: historical = events whose year is ≤ publication_year_proxy). This is a known English-pattern gap (METHOD.md “English-language caveat”), not a true pre-publication historical claim: 2024 is the citation year of the research being endorsed, and the result (productivity growth over the next 10 years) remains future from both 2024 and 2025.

Action at import: do **not** retokenize or drop 2024 from the quote to force `resolvable=true`. Keep the full quote. If the item is excluded, record it in policy_report / this audit as a screening error and use human review to decide re-inclusion without changing toolkit 85e6da1. Toolkit is not modified.

## Previous persisted quote (superseded)
```
{
  "id": "txt-00013",
  "predictions": [
    {
      "q": "Although some AI experts predict significant economic gains from AI, OECD (2024[24]) research indicates more tepid growth, estimating annual productivity growth due to AI ranging between 0.25-0.6 percentage points over the next 10 years in the most AI-ready countries.",
      "k": "prediction",
      "t": "forecast",
      "a": "author_endorsed",
      "sp": "OECD",
      "c": "Annual productivity growth due to AI will range between 0.25 and 0.6 percentage points over the next 10 years in the most AI-ready countries.",
      "ch": "points over the next 10 years",
      "h": "the next 10 years",
      "time_text": "the next 10 years",
      "conf": "medium",
      "f": true,
      "x": "The 2025 report contrasts unnamed experts' predictions of large AI economic gains with OECD (2024[24]) research — Filippucci, Gal and Schief, Miracle or Myth? (OECD AI Papers No. 29, published 22 November 2024) — which estimates more tepid annual productivity growth of 0.25-0.6 percentage points over the next 10 years in the most AI-ready countries. The report presents this as the Organisation's own research finding (author_endorsed), not as a new estimate dated from 18 September 2025. The 'next 10 years' window is therefore the 2024 paper's horizon (approximately late 2024 into the mid-2030s), still only partly elapsed at the 2026-11-15 cutoff.",
      "reference_resolutions": [
        {
          "expression": "the most AI-ready countries",
          "referent": "countries most prepared to adopt and use artificial intelligence, as described in the cited OECD (2024[24]) research (Filippucci, Gal and Schief, OECD AI Papers No. 29); that paper's main 0.25-0.6 pp. range is for US total-factor productivity, with other economies described as similar but somewhat lower",
          "support_quote": "in the most AI-ready countries"
        },
        {
          "expression": "OECD (2024[24]) research",
          "referent": "Filippucci, F., P. Gal and M. Schief (2024), “Miracle or Myth? Assessing the macroeconomic productivity gains from Artificial Intelligence”, OECD Artificial Intelligence Papers, No. 29, OECD Publishing, Paris, https://doi.org/10.1787/b524a072-en.",
          "support_quote": "OECD (2024[24]) research"
        }
      ],
      "unresolved_references": [],
      "cond": "",
      "m": "unknown",
      "method_basis": "unknown",
      "r": "A dated, later-checkable quantitative result that the 2025 report endorses from OECD (2024[24]) research: AI-driven annual productivity growth of 0.25-0.6 percentage points over the next 10 years in the most AI-ready countries. The ten-year window is anchored to the cited 2024 paper (published 22 November 2024), not reset at this book's 2025-09-18 publication date.",
      "screening_note": "Deterministic year-screen in prepare_book.rule_quote will likely mark this historical: mentioned_years includes 2024, publication_year_proxy is 2025, and English 'the next 10 years' does not match Chinese _FUTURE_WINDOW. This is a known English-language pattern gap (METHOD.md), not a true pre-publication historical claim. Do not drop 2024 from the quote to bypass the screen. Record as screening error at import; keep the full quote and attribution; human-review if the item is excluded from claims.jsonl."
    }
  ]
}
```

## Current persisted quote
```
{
  "q": "Although some AI experts predict significant economic gains from AI, OECD (2024[24]) research indicates more tepid growth, estimating annual productivity growth due to AI ranging between 0.25-0.6 percentage points over the next 10 years in the most AI-ready countries.",
  "k": "prediction",
  "t": "forecast",
  "a": "author_endorsed",
  "sp": "OECD",
  "c": "Annual productivity growth due to AI will range between 0.25 and 0.6 percentage points over the next 10 years in the most AI-ready countries.",
  "ch": "points over the next 10 years",
  "h": "the next 10 years",
  "time_text": "the next 10 years",
  "conf": "medium",
  "f": true,
  "x": "The 2025 report contrasts unnamed experts' predictions of large AI economic gains with OECD (2024[24]) research — Filippucci, Gal and Schief, Miracle or Myth? (OECD AI Papers No. 29, published 22 November 2024) — which estimates more tepid annual productivity growth of 0.25-0.6 percentage points over the next 10 years in the most AI-ready countries. The report presents this as the Organisation's own research finding (author_endorsed), not as a new estimate dated from 18 September 2025. The 'next 10 years' window is therefore the 2024 paper's horizon (approximately late 2024 into the mid-2030s), still only partly elapsed at the 2026-11-15 cutoff.",
  "reference_resolutions": [
    {
      "expression": "the most AI-ready countries",
      "referent": "countries most prepared to adopt and use artificial intelligence, as described in the cited OECD (2024[24]) research (Filippucci, Gal and Schief, OECD AI Papers No. 29); that paper's main 0.25-0.6 pp. range is for US total-factor productivity, with other economies described as similar but somewhat lower",
      "support_quote": "in the most AI-ready countries"
    },
    {
      "expression": "OECD (2024[24]) research",
      "referent": "Filippucci, F., P. Gal and M. Schief (2024), “Miracle or Myth? Assessing the macroeconomic productivity gains from Artificial Intelligence”, OECD Artificial Intelligence Papers, No. 29, OECD Publishing, Paris, https://doi.org/10.1787/b524a072-en.",
      "support_quote": "OECD (2024[24]) research"
    }
  ],
  "unresolved_references": [],
  "cond": "",
  "m": "unknown",
  "method_basis": "unknown",
  "r": "A dated, later-checkable quantitative result that the 2025 report endorses from OECD (2024[24]) research: AI-driven annual productivity growth of 0.25-0.6 percentage points over the next 10 years in the most AI-ready countries. The ten-year window is anchored to the cited 2024 paper (published 22 November 2024), not reset at this book's 2025-09-18 publication date.",
  "screening_note": "Deterministic year-screen in prepare_book.rule_quote will likely mark this historical: mentioned_years includes 2024, publication_year_proxy is 2025, and English 'the next 10 years' does not match Chinese _FUTURE_WINDOW. This is a known English-language pattern gap (METHOD.md), not a true pre-publication historical claim. Do not drop 2024 from the quote to bypass the screen. Record as screening error at import; keep the full quote and attribution; human-review if the item is excluded from claims.jsonl."
}
```
