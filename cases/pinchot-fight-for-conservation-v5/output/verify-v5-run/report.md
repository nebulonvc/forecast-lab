# 实际核验方法与结果

完整阅读本书45/45个3500字符body（前后600字符context仅助理解），非关键词选句。原始73条由原validate_chunk_predictions与claims_from_results确定性排除5条（格言2、机制1、规范2），保留全部68条且全部resolvable；ASSESS不再排除，没有语义去重或duplicate排除，自动重叠去重0。TXT为单栏，不涉及双栏重排/OCR。实际使用Exa新密钥路径，未使用DeepSeek。每条先写scope及正反查询，再从真实返回URL中选不超过8个来源，读取存档后逐条写中文理由、限制和六维审查。第一轮136个计划查询中135成功，#10 support中断保留不确定请求且未重试；第二轮换查询补足，并对仍缺证据的主题作自适应补查，共29条58个第二轮查询，未用第三轮。总计193个成功查询、128个URL/128份来源存档；Exa contents通常至多12000字符，森林管理历史一页另以urllib+BeautifulSoup抓完整公开HTML。所有判分事实限定存档可见内容。无日期方向按1910→2026-11-15窗口，未触发条件不给正确或错误，未知条件可观察后果仅给部分符合；无终点及缺口明确者保守未定。此为有相关性的回顾性父记录计数，不是独立预测技巧估计。

{
  "complete": true,
  "tasks": 68,
  "assessed": 68,
  "successful_queries": 193,
  "planned_round1_queries": 136,
  "round1_successful_queries": 135,
  "interrupted_unknown_first_support_claim": 10,
  "round2_claim_indices": [
    1,
    3,
    4,
    7,
    10,
    12,
    13,
    14,
    16,
    17,
    18,
    19,
    20,
    23,
    24,
    25,
    26,
    34,
    35,
    38,
    39,
    48,
    50,
    51,
    54,
    56,
    59,
    61,
    63
  ],
  "round2_successful_queries": 58,
  "third_round_claims": [],
  "selected_urls": 128,
  "forecasts": 68,
  "decidable": 43,
  "verdicts": {
    "暂无法判断": 25,
    "正确": 16,
    "部分符合": 21,
    "错误": 6
  },
  "trend_aligned_n": 0,
  "duplicates_excluded": 0,
  "actual_source_method": "Exa search / contents; one already-selected public HTML page fetched completely via urllib+BeautifulSoup after contents truncation",
  "estimated_exa_cost_USD_not_reconciled": 1.479,
  "unknown_reserved_USD_not_reconciled": 0.007
}


context清空后，用原toolkit.extraction_provenance函数重绑source-fields receipt（共204条历史/派生记录，实时claims为68条），未改quote、位置、类型、归属或判分；旧新receipt仅保留hash和字段元数据。随后重新apply→check→report，并逐条validate_extraction_provenance及原确定性抽取回放通过。
