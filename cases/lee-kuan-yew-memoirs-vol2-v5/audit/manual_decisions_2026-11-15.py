# -*- coding: utf-8 -*-
"""Manual decisions for lee-kuan-yew-memoirs-vol2-v5 (From Third World to First, 2000-09), 2026-11-15.
Memoir rule: judgments the author made or reports from 1965-2000 whose outcome was settled before the
book's publication are retrospective narration and are excluded; only claims whose horizon runs past
publication are judged."""
AU = 'manual-audit-2026-11-15'
MA = 'manual-assistant-2026-11-15'
IH = 'manual-audit-2026-11-15-implicit-horizon'

_R = '回忆录中对过去当时判断的叙述，结果在本书2000年出版前已经揭晓，不是本书对出版之后的预测。'
RETRO = [1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 18, 19, 21, 22, 24, 25, 26, 27, 28, 29, 31, 32, 33, 39, 40,
         44, 45, 46, 49, 53, 55, 56, 57, 58, 66, 75, 77]
NF = {i: ('retrospective', _R) for i in RETRO}
NF.update({
    13: ('normative', '“如果不摈弃对外来人才的偏见，偏见将成为绊脚石”是劝诫性条件句，没有可观察的结果。'),
    15: ('normative', '“如果把讲礼貌当做生活方式，新加坡将更愉快”是劝诫，不是预测。'),
    48: ('duplicate', '与第47条（澳新两国将成为亚欧峰会成员）重复。'),
    78: ('hope', '“希望将来遭遇危机时物色的人才能脱颖而出”是愿望，不是预测。'),
    82: ('aphorism', '“工业社会正在让位给知识社会，新的分野是有知识或没知识”是概括性论断，没有可判定的口径。'),
})

def ev(*pairs):
    return list(pairs)

_UND = lambda why, tag=MA: ('暂无法判断', False, why, tag, ev())

V = {
    11: _UND('“行动党能否继续主导政坛取决于它如何回应教育程度更高的人民”是条件分析。行动党至今仍执政，但得票率在2011和2020年明显下降，因果关系无法从公开资料中判定，暂无法判断。'),
    59: _UND('条件句：一旦在南沙发现石油天然气，和平中立区计划就不太可能实现。南沙争端在窗口内加剧，但“发现油气”这一前提是否成为原因难以核实，暂无法判断。'),
    76: _UND('“在上海等沿海城市设施建成之前，经香港的商业活动是香港繁荣的保证”，终点（上海设施建成）没有清楚口径，暂无法判断。'),
    14: _UND('“再过两代人，华语将成为新加坡华人的母语”，两代人约五十年，期限未到。需要说明，窗口内新加坡华人家庭中以英语为主要家庭用语的比例持续上升，方向与原文相反，但不提前判错。', AU),
    80: _UND('“新加坡作为主权国家可能会消失”是没有期限的可能性提醒，窗口内没有发生，也不足以否定，暂无法判断。', AU),
}

RR = {}
