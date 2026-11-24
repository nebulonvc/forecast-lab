# -*- coding: utf-8 -*-
"""Manual decisions for lee-kuan-yew-memoirs-vol1-v5 (The Singapore Story, 1998-09-16), 2026-11-15.
Memoir rule: predictions the author made or reports from 1940s-1965 whose outcome was already
settled before the book's publication (1998) are retrospective narration, not forecasts made by
the book, and are excluded. Only claims whose horizon runs past 1998-09-16 are judged."""
AU = 'manual-audit-2026-11-15'
MA = 'manual-assistant-2026-11-15'
IH = 'manual-audit-2026-11-15-implicit-horizon'

KEEP = {7, 53, 55}
NF = {i: ('retrospective', '回忆录中对1940–1965年间当时判断的叙述，结果在本书1998年出版前已经揭晓，不是本书对出版之后的预测。')
      for i in range(1, 56) if i not in KEEP}

def ev(*pairs):
    return list(pairs)

V = {
    7: ('暂无法判断', False,
        '作者在1998年写道，由于日本政界、学界和媒体拒绝承认过去的罪行，人们不能不担心日本“可能会重蹈覆辙”。这是一种担忧而不是有期限的预测。窗口内日本没有对外侵略，但2022年后防卫开支和反击能力明显扩张，两方面都不足以判定，暂无法判断。',
        MA, ev()),
}

RR = {}
