# 验收说明：mill-principles-of-political-economy r2

这是独立 QA「待修订」之后的最小修订。原 ZIP 不覆盖，sha256 仍是 `53c915d7a1ea13fe0f3cdec9e28f077025b6a0d4414f0f8bbe5c237b71925542`。本包不记通过。r1 说明留在 `audit/history-r1/验收说明.md`。r1 门日志留在 `audit/gates/history-r1/`。旧收据 `output/accepted_assessment_79e8860209bd.jsonl` 保留。

## 只改三处裁决

三条都改为暂无法判断，不另打正确或错误。旧裁决和当时的六项自检留在各阶段 `revision_trail`。

- `txt-5386516eaf-001974084-001974155`：批发、零售和汽车服务的就业份额，以及伦敦零售人数，不是合作运动导致纯分配者人数缩小。
- `txt-5386516eaf-001974735-001974807`：制造业就业下降和劳动力转向服务，不是合作制度把分配者释放后转入生产。直接效果没有观察到。
- `txt-5386516eaf-001985266-001985317`：OECD 说竞争政策仍有必要，不是竞争本身对进步不可或缺。

其余评分没有重搜、重研。

## 日期

`ev-london-retail` 页内印 Greater London Authority September 2007。`date` 改为 `2007-09`，精度为 month。不编日。

## 检索收据

只有 `audit/search-log.jsonl` 有执行记录，共 7 个 ID、14 行。索引在 `audit/search-receipt-index.json`。没有找到其他工具返回收据。其余阶段写明无 `executed=true`。本次不回填。

## 计数

85 条。prediction 73，unclear 12。display：正确 2，趋势符合 0，部分符合 14，错误 1，暂无法判断 68。

新收据 `output/accepted_assessment_c656e423f66a.jsonl`。

## 本轮门

| 门 | 结果 |
|---|---|
| apply | 退出码 0 |
| check | `OK: 85 claims; 68 verified evidence records` |
| report | 退出码 0，与 summary 一致 |
| 单测 | 209 项，退出码 0 |
| inspect | 错误 0 |
| 连续 300 字 | DISALLOWED_GE_300 0 |
| 密钥字面 | 命中都是正文连字符，不是密钥 |

未调用 DeepSeek，未 push，未开 PR。锁包未改。
