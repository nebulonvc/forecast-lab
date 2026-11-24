# 实际方法

原PDF与队列SHA256完全相同，pdftotext -enc UTF-8默认布局得到391316字符TXT；113/113个3500字符body依次完整阅读（含脚注、参考文献、索引及出版广告），非关键词选句，无OCR。手写100条，原validate_chunk_predictions全部exact对齐、无拒绝；原claims_from_results自动historical排除7、重叠去重4，保留89候选（45resolvable、44unclear）。扩充SAI、化石企业、Ubuntu等短指代为原TXT连续quote，书目旧年份随扩引触发7项原historical筛选，存在误杀未来判断的已知限制，未修改分类器或人为恢复。txt-00059一条SAI连续扩引向前跨body起点213字符，仍处原600字符context范围，原代码标in_body=true；此为补主体支持的跨块引文而非拼接，所有位置均在原TXT逐字核对。44项原unclear逐项记录归属或不可核验方向的边界，未把其冒作已判预测；下文45是resolvable核验子集，非全书候选数。未进行人工语义去重，ASSESS duplicate为0。
每项先写scope及正反各1查询，首轮90次全部成功；第二轮39项各改变策略实际仅执行1条新查询（不是每项两条），包括针对条件是否满足、出版后部署及缺失结果指标的补查，共129次成功查询，无第三轮。SELECT每项最多8URL且仅来自真实返回，103个URL全部存档、SHA256记录于evidence，135条逐源注释均定位实际存档完整句子。读取返回与存档可见段落后由助手写判定、限制与六维复核；组装脚本只辅助结构和引句定位，不以脚本默认标签或自动pass代替语义判断，未用DeepSeek。Exa contents通常截至12000字符，Guardian仅1000字符开头，未抓部分不用；已选Repórter Brasil公开PDF另用curl下载并pdftotext完整转换。
不将气候模型、普通生物质能源或动物人工子宫实验当作相应人类/地球尺度技术已经部署；不把出版前实验因论文后来发表而当出版后验证。平台主权化、机器人模仿与尊重需求等虽有相关研究，因对象、时序或强度指标不对应仍记未定。5项正确、1项趋势、2项部分、0项错误、37项未定；decidable仅8，主题相关且条件句多，比例不代表独立预测技巧。未定各有具名缺口并完成第二轮。
全部context及派生context清空；113份全文plans与341项请求/响应/checkpoint等缓存仅保留worker本地，case/bundle不含全书。带认证回调查询的1个未选URL仅在交付检索记录中移除查询参数，原始缓存留worker私有；实际选源URL不变。来源用干净稳定URL，不复述先前临时签名下载地址。

{
  "complete": true,
  "all_candidates": 89,
  "resolvable_tasks": 45,
  "assessed_including_original_unclear": 89,
  "original_unclear_nonforecast": 44,
  "forecasts": 45,
  "decidable": 8,
  "display_verdicts": {
    "correct": 5,
    "trend": 1,
    "partial": 2,
    "wrong": 0,
    "undetermined": 37
  },
  "verdicts": {
    "暂无法判断": 37,
    "正确": 5,
    "部分符合": 3
  },
  "trend_aligned_n": 1,
  "successful_search_queries": 129,
  "round1_queries": 90,
  "round2_claim_indices": [
    1,
    2,
    3,
    6,
    7,
    8,
    9,
    10,
    11,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    23,
    24,
    25,
    26,
    27,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45
  ],
  "round2_queries": 39,
  "third_round_claims": [],
  "selected_urls": 103,
  "evidence_records": 103,
  "evidence_notes": 135,
  "automatic_overlap_dropped": 4,
  "manual_semantic_deduplications": 0,
  "assessment_duplicate_exclusions": 0,
  "estimated_search_cost_USD_not_bill": 0.903,
  "actual_source_method": "Exa search/contents; one already-selected public PDF supplemented completely by curl and pdftotext; raw caches private, sanitized returned search records included"
}