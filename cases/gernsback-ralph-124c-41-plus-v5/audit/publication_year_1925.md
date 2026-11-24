# 出版年口径审计（不改变已接受 config）

记录时间：2026-11-16 15:48:23 CST（Asia/Shanghai）
书 id：gernsback-ralph-124c-41-plus
已接受口径（保持不变）：`publication_date` 1925-01-01，`publication_year_proxy` 1925，cutoff 2026-11-15。

## 队列

- `orig_pub_date`：`1925 (serialized 1911)`
- `notes`：`1911 年起连载、1925 年成书. Serialized from 1911; first book edition 1925.`
- README.md「Oddities」：`Gernsback serialized 1911, book 1925`
- WORKER_BRIEF：观察窗口 = original publication → 2026-11-15

## METHOD

- `publication_year_proxy` 为整数，须写入 config；`historical` 含出版年及之前（年份 ≤ proxy）的事件。
- 「Front and back matter (`matter_spans`) are skipped. Preface, acknowledgements and afterword are never forecasts.」
- 1950 再版序、1925 初版序、Lee de Forest 与 Fletcher Pratt 前言按此条排除，不抽取为预测（即使序中有作者事后评述）。

## 实际文本版本

- 本 TXT 为 Project Gutenberg #60944，`cache/epub/60944/pg60944.txt`，sha256 与队列一致。
- 版权页：Copyright 1925 / Second Edition Copyright 1950（Frederick Fell）。排印形态是 **1950 第二版**。
- **1925 初版序**（正文前附文）明确：因科学进步并为扩大读者，「to rewrite much of the story and to make many changes」，但「the ideas and conceptions embodied in the original manuscript have been little altered」。故 1925 单行本已对 1911 连载作过改写。此为已接受 1925 口径的主要文本依据（与队列「1925 年成书」一致）。
- **1950 再版序**（Hugo Gernsback, New York, May 1950）：称「reading proofs for the 1950 edition, after a lapse of 25 years」；回顾 1911 写作、指出早期预测的 minor technical flaws，并说「on the whole I probably could not do much better today」。序文**没有**像 1925 序那样声明再次改写故事正文。
- 正文内有编辑性脚注（如 Footnote 1：写作时还没有名为 New York News 的报纸；Footnote 2：五十单位合 72°F）。这些是附加说明，尚未用作预测句；它们可能为再版或排印时所加，构成「正文是否经 1950 修订」的残余歧义，但不单独改变全书窗口。

## 歧义与处理（不自行改口径）

- 歧义：源文件是 1950 第二版排印；若日后证实某段故事正文相对 1925 有实质性改写，则该段窗口需再审计。目前 1950 序只证明作者读过 1950 校样并新写序言，未证明正文第二次改写。
- 对照：README 对 Zakaria 写「Only the 2008 scan is in the repo. Score that text only。」——那是「库中仅有该版」的特例说明。Gernsback 队列仍将作品年份标为 1925（serialized 1911），与「第一版单行本」口径一致。
- **本审计不修改已接受的 1925 proxy。** 1950/1925 序与两篇他人前言继续作书前附文排除。

## 正文中晚于 1925 的编辑性脚注（补充，仍不改口径）

- Footnote 6（约偏移 170558）：“When this was written gold coins were legal tender. Gold payments were outlawed by Congress in 1933.” 1933 年晚于 1925 初版，说明至少这条脚注是 1925 年之后（与 1950 再版排印相符）加上的。本脚注未用作预测，亦不据此把全书 `publication_year_proxy` 改为 1950。
