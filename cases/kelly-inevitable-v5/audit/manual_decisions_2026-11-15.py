# -*- coding: utf-8 -*-
"""Manual decisions for kelly-inevitable-v5, 2026-11-15 (Asia/Shanghai)."""
AU = 'manual-audit-2026-11-15'
MA = 'manual-assistant-2026-11-15'
IH = 'manual-audit-2026-11-15-implicit-horizon'

NF = {
    15: ('aphorism', '“我们是，也将会是永远的菜鸟”是格言式表述，没有可观察的结果。'),
    21: ('rhetorical', '“未来的人们会感慨当时有多少可能性”是修辞性设想，无法验证。'),
    98: ('philosophical', '“没有任何著作和理念是出类拔萃的，一切优秀事物都是生态系统”是观念主张，不是可判定的预测。'),
    251: ('philosophical', '“问题的数量会以比知识更快的指数速率增长”没有可测量的口径，无法判定。'),
}

def ev(*pairs):
    return list(pairs)

_UND = lambda why, tag=MA: ('暂无法判断', False, why, tag, ev())

V = {
    # ---- stuck ----
    55: _UND('期限是“本世纪结束前”，远未到期。'),
    66: _UND('期限是2050年，未到期。'),
    138: ('部分符合', True,
          '原文说尽管有人阻挡，共享仍会持续增长。窗口内开源与开放模型共享持续扩张，Hugging Face 托管模型在2024年9月突破100万个；但开源维护者流失和倦怠问题突出，部分领域转向闭源，判趋势符合。',
          MA, ev(('https://arstechnica.com/information-technology/2024/09/ai-hosting-platform-surpasses-1-million-models-for-the-first-time/', 'Ars Technica (26 Sep 2024): Hugging Face surpasses 1 million AI models.'),
                 ('https://www.sonarsource.com/blog/maintainer-burnout-is-real/', 'Sonar (25 May 2023): almost 60% of maintainers have quit or considered quitting.'))),
    155: ('部分符合', True,
          '原文说聪明的过滤器会应用到任何需要大量选择的领域，凡人们想要个性化的领域都会出现过滤服务。窗口内推荐系统从媒体扩展到零售、旅游、社交电商等领域，生成式模型也被引入推荐，方向一致；但“任何领域”过于绝对，旅游等行业仍处在试验阶段，判趋势符合。',
          MA, ev(('https://introspectives.github.io/2024/uploads/adoption_of_recommender_systems.pdf', 'Shah & González-Fierro (Microsoft, 2024): Adoption of recommendation systems: observations and trends.'),
                 ('https://arxiv.org/abs/2406.06475', 'arXiv 2406.06475 (Jun 2024): Landing generative AI in social and e-commerce recommender systems.'),
                 ('https://www.atalayar.com/en/economy-and-business/improving-customer-experience-the-key-to-ai-in-the-tourism-sector/20240723163000203225.html', 'Atalayar (23 Jul 2024): 33% of tourism companies already experimenting with AI.'))),
    235: _UND('“一旦置身于全球实时同步的社会，之前不可能的事将以爆发方式变成现实”的前提和结果都没有可观察的口径，暂无法判断。'),
    236: ('错误', False,
          '原文没写期限，说随着解决冲突的新途径出现，有组织战争的吸引力和作用会越来越弱。按出版（2016）至截止日的窗口，UCDP 记录国家间和国内武装冲突数在2023–2024年升至1946年以来最高，俄乌、加沙等战争规模巨大，方向与预测相反。',
          MA, ev(('https://www.uu.se/en/press/press-releases/2025/2025-06-11-ucdp-sharp-increase-in-conflicts-and-wars', 'Uppsala University / UCDP (11 Jun 2025): Sharp increase in conflicts and wars.'),
                 ('https://journals.sagepub.com/doi/full/10.1177/00223433251345636', 'Journal of Peace Research (2025): Organized violence 1989–2024.'))),
    259: _UND('“全球心智的聚拢将被当作这个星球上迄今最重要的事件”是对未来历史评价的判断，窗口太短，暂无法判断。'),
    # ---- audit of completed items ----
    64: _UND('“无论医生、律师、建筑师、记者还是程序员，机器人都将历史性地接管你的工作”是作者对本世纪的长期判断（同章说本世纪末70%职业被取代），原文没给近期期限，不宜用十年窗口判错。', AU),
    73: _UND('“未来90%的同事将是看不见的机器”没写期限，是长期设想；窗口内远未达到，但不提前判错。', AU),
    143: _UND('期限是“50年之内”（约2066年），远未到期。机器按现状判错，口径不当。', AU),
    196: _UND('“将来的办公室职员无需键盘、改用手势语言”是没给期限的长期设想；窗口内键盘仍占主导，但不提前判错。', AU),
    269: _UND('原文说“再过几十年”这个整体都不太可能停止运转，期限未到。窗口内互联网只有局部、短暂的中断，方向暂时一致，但不提前判正确。', AU),
    271: _UND('“硬奇点不太可能实现”是没有期限的否定性判断。窗口内没出现递归自我改进的超级智能，但这不能证明它长期不会实现，暂无法判断。', AU),
    85: ('部分符合', True,
         '“知识将支配原子”是高度概括的判断。WIPO 数据显示2008–2024年无形资产投资增速约为有形资产的3.7倍，方向一致；但“支配”没有清楚口径，由正确改为趋势符合。',
         AU, ev()),
    199: ('部分符合', True,
          '期限是“未来的几十年”，尚未到期。窗口内联网设备从约70亿台增至约200亿台，方向持续，由正确改为趋势符合。',
          AU, ev()),
}

RR = {}
