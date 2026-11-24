# 自动判断流程诊断

只统计程序记录，不人工判定预测，也不调用付费API。后面的运行按预测ID覆盖前面的运行；费用保留全部尝试。

独立预测：53；任务尝试：72。

|阶段|判断分布|
|---|---|
|初判|{"趋势符合": 32, "部分符合": 2, "暂无法判断": 16, "错误": 2, "正确": 1}|
|最后草稿|{"正确": 2, "暂无法判断": 42, "趋势符合": 8, "部分符合": 1}|
|最终输出|{"暂无法判断": 53}|

末端路径（互斥统计）：{"mechanical_downgrade": 3, "draft_already_unresolved": 42, "last_review_rejected": 8}

路径顺序：技术未完成 → 已判定 → 末稿已未定 → 最后复核拒绝 → 机械校验直接降级 → 无法归因；这不是对研究判断的正确性评分。

检索统计：{"queries": 212, "query_states": {"completed": 212}, "tasks_without_query_log": 0, "query_roles": {"support": 106, "counter": 106}, "reported_hits": 1060, "known_hit_subtotal": 1060, "missing_hit_counts": 0, "tasks_with_both_query_roles": 53, "new_source_records": 290, "tasks_with_new_source": 53, "source_statuses": {"retrieved": 290}, "source_date_statuses": [{"source_kind": "exa_contents", "date_status": "known", "count": 127}, {"source_kind": "exa_contents", "date_status": "unknown", "count": 163}, {"source_kind": "previously_registered_excerpt", "date_status": "known", "count": 98}, {"source_kind": "previously_registered_excerpt", "date_status": "unknown", "count": 48}], "source_bodies_present": 0, "context_truncation_not_recorded": 436, "context_truncation_not_recorded_scope": "Candidate field only; absence does not mean stage coverage is missing. See context_coverage.", "provider_limit_reached": 145}

按阶段准备的上下文覆盖：{"tasks_total": 53, "tasks_with_recorded_stages": 0, "tasks_without_recorded_stages": 53, "tasks_missing_coverage_field": 53, "tasks_invalid_coverage_field": 0, "tasks_empty_coverage": 0, "by_stage": {}, "meaning": "Prepared stage/round snapshots, not proof of successful API consumption. Sources appearing in multiple snapshots count repeatedly; byte totals refer to the supplied source body, not necessarily the full original page. Missing byte values stay null."}

候选记录缺少 context_truncated 字段，不等于任务没有阶段截断记录；上表独立读取 context_coverage。相同来源在多轮出现会重复计数，记录本身不证明该次 API 已成功读取。

费用（原币种；null 表示有缺失）：{"deepseek_CNY": {"estimated_cost_CNY": {"total": 6.93277892, "known_subtotal": 6.93277892, "missing_runs": 0}, "budget_committed_CNY": {"total": 6.93277892, "known_subtotal": 6.93277892, "missing_runs": 0}, "unknown_or_inflight_reserved_CNY": {"total": 0, "known_subtotal": 0, "missing_runs": 0}}, "exa_USD": {"estimated_cost_USD": {"total": 2.18, "known_subtotal": 2.18, "missing_runs": 0}, "budget_committed_USD": {"total": 2.18, "known_subtotal": 2.18, "missing_runs": 0}, "unknown_or_inflight_reserved_USD": {"total": 0, "known_subtotal": 0, "missing_runs": 0}}}

同材料四臂 API 对照：{"selected_samples": 0, "all_four_completed": 0, "all_four_same_material_hash": 0, "all_four_same_protocol": 0, "all_four_excluded_schema_repair_or_missing": 0, "comparison_policy": "Primary comparisons require completed arms, identical material hashes and explicit schema_repaired=false on both sides. Repaired or unrecorded protocols remain counted as exclusions.", "arms": {"legacy_hint": {"statuses": {}, "completed": 0, "failed_or_missing": 0, "schema_repaired": 0, "schema_repair_flag_missing": 0, "decisions": {}, "nonpass_checks": []}, "legacy_nohint": {"statuses": {}, "completed": 0, "failed_or_missing": 0, "schema_repaired": 0, "schema_repair_flag_missing": 0, "decisions": {}, "nonpass_checks": []}, "shared_hint": {"statuses": {}, "completed": 0, "failed_or_missing": 0, "schema_repaired": 0, "schema_repair_flag_missing": 0, "decisions": {}, "nonpass_checks": []}, "shared_nohint": {"statuses": {}, "completed": 0, "failed_or_missing": 0, "schema_repaired": 0, "schema_repair_flag_missing": 0, "decisions": {}, "nonpass_checks": []}}, "paired_changes": [{"left": "legacy_hint", "right": "legacy_nohint", "completed_pairs": 0, "all_material_hash_pairs": 0, "same_material_pairs": 0, "same_protocol_pairs": 0, "excluded_schema_repair_or_missing_pairs": 0, "excluded_schema_repair_pairs": 0, "excluded_missing_schema_repair_flag_pairs": 0, "changed_decisions_same_material": 0, "transitions_same_material": []}, {"left": "shared_hint", "right": "shared_nohint", "completed_pairs": 0, "all_material_hash_pairs": 0, "same_material_pairs": 0, "same_protocol_pairs": 0, "excluded_schema_repair_or_missing_pairs": 0, "excluded_schema_repair_pairs": 0, "excluded_missing_schema_repair_flag_pairs": 0, "changed_decisions_same_material": 0, "transitions_same_material": []}, {"left": "legacy_hint", "right": "shared_hint", "completed_pairs": 0, "all_material_hash_pairs": 0, "same_material_pairs": 0, "same_protocol_pairs": 0, "excluded_schema_repair_or_missing_pairs": 0, "excluded_schema_repair_pairs": 0, "excluded_missing_schema_repair_flag_pairs": 0, "changed_decisions_same_material": 0, "transitions_same_material": []}, {"left": "legacy_nohint", "right": "shared_nohint", "completed_pairs": 0, "all_material_hash_pairs": 0, "same_material_pairs": 0, "same_protocol_pairs": 0, "excluded_schema_repair_or_missing_pairs": 0, "excluded_schema_repair_pairs": 0, "excluded_missing_schema_repair_flag_pairs": 0, "changed_decisions_same_material": 0, "transitions_same_material": []}], "limitation": "Paired changes measure recorded prompt/hint sensitivity, not correctness against an independent truth standard."}

现有记录只能显示状态变化，不能证明 prompt 导致错误，也不能因为更多结论可判定就认为修复成功。需冻结相同材料做 API 对照。旧版日期暴露是旧规则的重建；新版优先读取记录的 trace，缺失时不套用旧规则。

[完整结构统计、交叉表及限制](diagnosis.json)
