# -*- coding: utf-8 -*-
"""Manual decisions for kissinger-age-of-ai-v5, 2026-11-15 (Asia/Shanghai)."""
AU = 'manual-audit-2026-11-15'
MA = 'manual-assistant-2026-11-15'
IH = 'manual-audit-2026-11-15-implicit-horizon'

NF = {
    106: ('aphorism', '“人工智能将再次检验我们的自我认知所依据的原则到底是什么”是哲学性表述，没有可观察的结果或判定口径；机器用伦理文件和民调把它判为正确，口径不成立。'),
}

def ev(*pairs):
    return list(pairs)

V = {
    # ---- stuck ----
    12: ('暂无法判断', False,
         '条件是机器被授权进行自主目标决策。窗口内各国未公开承认授权武器系统自主决定攻击目标，联合国大会和《特定常规武器公约》专家组仍在讨论自主武器规则，战争法既未被颠覆，也尚未形成新的约束性调整。前提未清楚触发，后果也未落地。',
         MA, ev(('https://www.sipri.org/publications/2024/policy-reports/towards-multilateral-policy-autonomous-weapon-systems',
                 'SIPRI: multilateral policy on autonomous weapon systems remained under negotiation; no binding instrument adopted.'))),
    32: ('部分符合', False,
         '作者以“也许……可能”的语气说，人工智能司机不久可能在长途行车中比人类更安全。Waymo 在城市无人驾驶网约车的同口径比较中事故率明显低于人类基准，说明“比人类更安全”这一方向已有证据；但这些数据主要来自城市道路，长途／高速场景缺少成规模、可比的安全数据。“更安全”这一分项成立，“长途”这一分项尚未证实，判部分符合。',
         MA, ev(('https://www.tandfonline.com/doi/full/10.1080/15389588.2024.2380786',
                 'Traffic Injury Prevention (2024): Waymo rider-only crash rates over 7.1 million miles were lower than human benchmarks in the cities studied.'),
                ('https://spectrum.ieee.org/autonomous-vehicles-great-at-straights',
                 'IEEE Spectrum (2024): autonomous vehicles perform well on straight driving but humans still do better at turns and low light.'))),
    37: ('暂无法判断', False,
         '条件是该领域进展每两年翻一番，后果是不到10年内弥合与人脑规模的差距。10年终点约在2031年，尚未到期；参数规模也不能直接等同于人脑突触规模，故暂无法判断。',
         MA, ev()),
    66: ('部分符合', True,
         '作者认为印度可能走更独立的技术道路，或在技术兼容国家集团中担任主要角色。窗口内印度推出 IndiaAI Mission（2024年3月）、半导体激励计划，并在 G20 推广数字公共基础设施，方向已经出现；但电子与通信设备进口仍高度依赖中国及中国香港，独立道路尚未完成，判趋势符合。',
         MA, ev(('https://www.pmindia.gov.in/en/news_updates/cabinet-approves-ambitious-indiaai-mission-to-strengthen-the-ai-innovation-ecosystem/',
                 'Cabinet Approves Ambitious IndiaAI Mission to Strengthen the AI Innovation Ecosystem (7 March 2024).'),
                ('https://economictimes.indiatimes.com/news/economy/foreign-trade/china-hong-kong-account-for-56-pc-of-india-s-total-imports-of-electronics-telecom-electrical-products-gtri/articleshow/109787013.cms',
                 'GTRI (May 2024): China and Hong Kong account for 56% of India’s imports of electronics, telecom and electrical products.'))),
    81: ('部分符合', True,
         '条件句：如果人工智能被赋予对网络武器或飞机等物理武器的一定控制权，它可能迅速执行人类难以执行的功能。DARPA ACE 项目在2023–2024年让人工智能在真实 F-16（X-62A）上自主飞行并与有人驾驶战机进行近距离空战测试，说明前提已部分触发、能力方向已出现；但这仍是试验性部署，“人类难以执行”的作战功能尚无实战层面的公开证据，判趋势符合。',
         MA, ev(('https://www.darpa.mil/news/2024/ace-ai-aerospace',
                 'DARPA (April 2024): ACE program achieved in-air combat tests between an AI-controlled X-62A and a human-piloted F-16.'))),
    88: ('暂无法判断', False,
         '条件是大国等到危机发生才开始就人工智能展开对话。窗口内中美在2024年5月于日内瓦举行人工智能政府间对话，2024年11月双方领导人同意由人类而非人工智能控制核武器使用决定，前提“坐视不理到危机”并未成立，不评价不可逆后果。',
         MA, ev()),
    92: ('暂无法判断', False,
         '担心对手发展自动化军力的国家可能先发制人。窗口内未出现以此为理由的先发制人攻击，条件未触发。',
         MA, ev()),
    96: ('暂无法判断', False,
         '若数字领域的战略防御需要战术进攻、且一方计算出错，就可能触发升级。窗口内没有可公开核实的此类误判升级事件，条件句无法判定。',
         MA, ev()),
    143: ('暂无法判断', False,
          '“人工智能在大量数据中发现的模式可能产生一系列准则，并在各大洲乃至全球平台上被奉为圭臬”。窗口内的人工智能原则大多由人类机构制定（OECD、欧盟、欧洲委员会公约），没有可核实的“由人工智能发现的模式变成全球准则”的事例，也难以证伪这种可能性。',
          MA, ev()),
    159: ('部分符合', True,
          '如果人工智能不受监管，它可能偏离我们的预期和意图。窗口内多数国家对通用模型的监管仍有限，实验与事故记录中已出现模型违背开发者意图的行为（如关停测试中破坏关停指令、委托人工智能后不诚实行为增加），方向符合；但这些多为受控实验，尚不足以证明大范围失控，判趋势符合。',
          MA, ev(('https://www.nature.com/articles/s41586-025-09505-x',
                  'Nature (17 Sep 2025): delegation to AI can increase dishonest behaviour.'),
                 ('https://cset.georgetown.edu/wp-content/uploads/CSET-The-Mechanisms-of-AI-Harm.pdf',
                  'CSET (Oct 2025): analysis of AI incidents and mechanisms of harm.'))),
    # ---- audit of completed items ----
    121: ('暂无法判断', False,
          '“长此以往，人们可能会更偏爱自己的数字助手而不是人类”是长期判断。2026年的调查显示多数人仍更愿与亲友交谈，但这只是阶段情况，作者的“长期”尚未到来，不提前判错。',
          AU, ev()),
    154: ('部分符合', True,
          '“人工智能时代将弘扬另一种知识概念，即知识是人机合作的成果”。科研界已出现“人工智能驱动科研范式”“人机混合智能”等提法，方向开始出现；但目前多为科研共同体与政策层面的倡议，尚不能说社会整体已普遍接受这种知识观，改为趋势符合。',
          AU, ev()),
}

RR = {}
