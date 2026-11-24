# work 脚本/答案一度缺失的事实记录（不推测原因）

记录时间：2026-11-16 15:48:23 CST（Asia/Shanghai）

## 事实

1. 本会话早些时候，已在 `/workspace/forecast-bot2-w25/work/answers/` 写入 txt-00008–00024（及 00001–00007、00090–00095），并在 `work/` 下写入 `extract_lib.py`、`write_008_016.py`、`write_017_024.py`、`print_chunk.py`、`find_quote.py`。当时 `validate_chunk_predictions` 已对 00008–00024 全部 kept。
2. 随后在准备/运行 `write_025_032.py` 时复查磁盘：`work/extract_lib.py`、`write_008_016.py`、`write_017_024.py` **已不存在**；`work/answers/` 中 **txt-00008–00024 已不存在**。仍在磁盘上的是：txt-00001–00007、txt-00090–00095，以及后来写入的 `write_025_032.py`。`print_chunk.py`、`find_quote.py`、`chunk_index.json`、`work/chunks/`、case 的 prepare 产物与 `books/`、`config.json` 仍在。
3. 本会话内没有留下删除这些文件的命令记录可引。此处只记录缺失当时的目录状态，不推断缺失原因。
4. 恢复来源：用本会话中已经跑通并打印过的 **start:end 字符偏移**（当时 `OK … start:end` 行，且 quote 由 `prepare_book.decode_text` 的原文切片给出），重新生成 00008–00024，并再对 `decode_text` 原文做逐字校验。不是凭记忆重写 quote。
5. 恢复后（2026-11-16 15:47–15:48 CST 复查）：00008–00024 共 30 条，quote 均在原文中、changes 均为 quote 内单行子串、`validate_chunk_predictions` 全部 kept、对齐偏移与原文字节一致、quote 长度均 ≤300。已有全部 00001–00032 与 00090–00095 共 44 条同样校验通过，issues=0。
6. 自恢复起，答案与脚本双写：`work/answers/` 与 `persist/answers/`（另 `persist/answers.jsonl`、`persist/scripts/`）。之后若再缺失，先把当时目录清单和哈希写入本目录审计，再恢复，并在回报中写明。

## 校验脚本结论（008–024）

- 检查条数：30
- issues：0
