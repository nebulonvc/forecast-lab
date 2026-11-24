# Human review: txt-00013 year-screen exclusion (historical)

Date: 2026-11-16 15:20 Asia/Shanghai (box-local). METHOD-only record. Toolkit 85e6da1 was not changed. The authentic `output/txt_import/policy_report.json` is also copied at `work/policy_report_authentic.json` and must be left unmodified as the pipeline's original output.

## What the pipeline did
`claims_from_results` / `classify_prediction` / `rule_quote` excluded this item as **historical** (`excluded_non_predictions.historical = 1`). The authentic excluded record keeps the complete quote, including the 2024 citation:

> Although some AI experts predict significant economic gains from AI, OECD (2024[24]) research indicates more tepid growth, estimating annual productivity growth due to AI ranging between 0.25-0.6 percentage points over the next 10 years in the most AI-ready countries.

Attribution in the authentic record: author_endorsed. reason: historical. The quote was not trimmed to bypass the screen.

## Why the screen fired (known English-language METHOD caveat)
Year-screen marks a quote historical when mentioned years exist, max(years) < publication_year_proxy (2025), and the Chinese `_FUTURE_WINDOW` regex does not match. Here max(years)=2024 < 2025, and the English phrase “the next 10 years” does not match `_FUTURE_WINDOW` (明年|后年|今后|未来|将来|…|\d+\s*年内|到 20xx|20xx 年 前/后/内…). This is a language-coverage gap in the existing METHOD implementation, not a reason to alter the toolkit or to drop “OECD (2024[24])” from the quote.

## Human reading of the claim
- The 10-year window is anchored to the cited paper: Filippucci, F., P. Gal and M. Schief (2024), “Miracle or Myth? Assessing the macroeconomic productivity gains from Artificial Intelligence”, OECD Artificial Intelligence Papers, No. 29, https://doi.org/10.1787/b524a072-en, OECD page date 22 November 2024. The 0.25–0.6 percentage-point range is that paper’s estimate over a 10-year horizon (mainly US TFP), approximately late 2024 into the mid-2030s — not reset at this book’s 2025-09-18 publication date.
- On a human reading, this is a then-still-open, later-checkable productivity-growth forecast, not a settled pre-publication historical fact.
- The book’s “most AI-ready countries” wording is this report’s paraphrase of the paper.

## What this review does and does not do
- It does **not** change toolkit 85e6da1, `_FUTURE_WINDOW`, or `classify_prediction`.
- It does **not** trim 2024 from the quote, invent a 2025-reset horizon, or recode attribution for scoring.
- It does **not** force re-inclusion into `claims.jsonl` or the scored set. The authentic policy_report exclusion stands as the pipeline result.
- Scoring and the canonical report therefore include only the five imported candidates (one resolvable author_endorsed forecast; four reported items demoted to unclear / not resolvable under v5). The 013 item is recorded here as a documented screening limitation / ambiguity.

## Ambiguity reported to the user
A human reviewer would treat 013 as a live 10-year productivity forecast anchored to November 2024, but the unchanged METHOD year-screen excludes it as historical because of the 2024 citation plus an English horizon that the Chinese future-window regex does not recognise. Per instruction, the authentic policy output is preserved and this record is the human-review path; no toolkit override was invented.
