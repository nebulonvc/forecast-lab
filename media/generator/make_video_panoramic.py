#!/usr/bin/env python3
"""
《百大精彩 · 五十翻车 · 未来方向全景》Anthropic x Kimi 科研档案风 + 双人神经网络中文配音版
输出:
  - media/videos/02-panoramic-330-forecasts.mp4
  - media/subtitles/02-panoramic-330-forecasts.srt
"""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw

import sci_theme as st

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_MP4 = BASE_DIR / "videos/02-panoramic-330-forecasts.mp4"
OUT_SRT = BASE_DIR / "subtitles/02-panoramic-330-forecasts.srt"
CURATED_JSON = Path(__file__).resolve().parent / "curated_330.json"
SCRATCH_DIR = BASE_DIR / ".build_cache/part2"

TOP_NODES = ["片头", "百大命中", "五十翻车", "未来方向", "总结"]
ARCHIVE = "FORECAST-LAB // 330 CURATED CASES"


def hdr(d, active=-1, all_done=False):
    st.draw_header(d, ARCHIVE, TOP_NODES, active_idx=active, all_done=all_done)


def draw_p0(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float, data):
    hdr(d, active=0)
    a0 = st.prog(t, 0.1, 0.5)
    a1 = st.prog(t, 0.25, 0.65)
    a2 = st.prog(t, 0.6, 0.65)
    st.draw_text(d, (st.W // 2, 165 + (1 - a0) * 14), "CURATED EMPIRICAL COMPENDIUM // N = 330", "mono", 18, st.TERRACOTTA, False, "mm", a0)
    st.draw_text(d, (st.W // 2, 242 + (1 - a1) * 20), "百大精彩 · 五十翻车 · 未来方向罗盘", "serif", 66, st.INK_DARK, True, "mm", a1)
    st.draw_text(d, (st.W // 2, 326 + (1 - a2) * 16), "从 132 部著作、8,130 条预测严格去重淘出的 330 条高含金量样本", "sans", 28, st.COBALT, True, "mm", a2)
    lp = st.prog(t, 0.5, 0.7)
    d.line([(st.W // 2 - int(360 * lp), 374), (st.W // 2 + int(360 * lp), 374)], fill=st.CARD_BORDER, width=1)

    cards = [
        ("PART A", 100, "条封神命中", "覆盖 42 部经典 · 看高手如何抓真信号", 1.2, st.FOREST, False),
        ("PART B", 50, "条大师翻车", "聚焦 46 部顶尖名家 · 拆解五大死因", 2.0, st.TERRACOTTA, True),
        ("PART C", 180, "条未来方向", "六大领域各 30 条 · 附 2026-2035 指标", 2.8, st.COBALT, False),
    ]
    cw, ch, gap = 470, 270, 50
    sx = (st.W - (3 * cw + 2 * gap)) // 2
    cy = 425
    for i, (pk, num, unit, desc, st_t, col, dark) in enumerate(cards):
        p = st.prog(t, st_t, 0.7)
        if p <= 0.01:
            continue
        x = sx + i * (cw + gap)
        y = cy + (1 - p) * 22
        bg_c = st.ANCHOR_DARK if dark else st.CARD_BG
        bd_c = st.ANCHOR_DARK if dark else st.CARD_BORDER
        st.draw_card(d, (x, y, x + cw, y + ch), fill=bg_c, outline=bd_c, radius=10, alpha=p)
        d.rectangle((x, y, x + cw, y + 4), fill=st.fade_color(col, p))
        st.draw_text(d, (x + 28, y + 26), pk, "mono", 15, col, True, "la", p, bg_c)
        cp = st.prog(t, st_t + 0.1, 1.1)
        val = int(round(num * cp))
        st.draw_text(d, (x + cw // 2, y + 108), str(val), "mono", 72, col if not dark else st.INK_LIGHT, True, "mm", p, bg_c)
        st.draw_text(d, (x + cw // 2, y + 174), unit, "serif", 28, st.INK_LIGHT if dark else st.INK_DARK, True, "mm", p, bg_c)
        st.draw_text(d, (x + cw // 2, y + 224), desc, "sans", 19, (188, 184, 176) if dark else st.INK_MUTED, False, "mm", p, bg_c)

    ab = st.prog(t, 4.4, 0.55)
    st.draw_text(d, (st.W // 2, 775), "全片逐页完整展示全部 330 条样本，文字全集与跟踪指标见配套总册", "sans", 22, st.INK_MUTED, False, "mm", ab)


def draw_p6(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float, data):
    hdr(d, active=2)
    st.draw_scene_title(d, "SECTION 02 // FAILURE TAXONOMY (N = 50)", "高手为何也会翻车：50 条大师失手死因拆解", "严选 46 部顶尖智库与名家代表作中的失误条目，统计其核心翻车模式", t)

    fc = data["part_b_failures"]
    order = sorted(fc.items(), key=lambda kv: kv[1], reverse=True)
    lx, ly, lw, lh = 80, 224, 1140, 665
    la = st.prog(t, 0.25, 0.45)
    st.draw_card(d, (lx, ly, lx + lw, ly + lh), alpha=la)
    st.draw_text(d, (lx + 34, ly + 32), "FAILURE MODES // TOP 50", "mono", 15, st.TERRACOTTA, True, "la", la, st.CARD_BG)
    st.draw_text(d, (lx + 34, ly + 56), "五大翻车死因分布", "serif", 28, st.INK_DARK, True, "la", la, st.CARD_BG)

    bar_x = lx + 410
    max_bw = 530
    for i, (fname, cnt) in enumerate(order):
        p = st.prog(t, 0.7 + i * 0.65, 0.55)
        bp = st.prog(t, 0.8 + i * 0.65, 0.85)
        y = ly + 126 + i * 102
        st.draw_text(d, (bar_x - 22, y + 22), fname, "sans", 22, st.INK_DARK if i == 0 else st.INK_BODY, i == 0, "rm", p, st.CARD_BG)
        bw = max(12, int((cnt / 30.0) * max_bw * bp))
        col = st.TERRACOTTA if i == 0 else st.AMBER
        d.rectangle((bar_x, y + 6, bar_x + bw, y + 38), fill=st.fade_color(col, p, st.CARD_BG))
        st.draw_text(d, (bar_x + bw + 14, y + 22), f"{int(round(cnt * bp))} 条 ({cnt/50*100*bp:.0f}%)", "sans", 21, col, True, "lm", p, st.CARD_BG)

    rx, rw = 1260, 580
    ra = st.prog(t, 4.2, 0.6)
    st.draw_card(d, (rx, ly, rx + rw, ly + lh), fill=st.ANCHOR_DARK, outline=st.ANCHOR_DARK, alpha=ra)
    d.rectangle((rx, ly, rx + rw, ly + 4), fill=st.fade_color(st.TERRACOTTA, ra))
    st.draw_text(d, (rx + 36, ly + 36), "CORE DIAGNOSTIC", "mono", 15, st.TERRACOTTA, True, "la", ra, st.ANCHOR_DARK)
    st.draw_text(d, (rx + 36, ly + 68), "为什么大师也会看走眼？", "serif", 30, st.INK_LIGHT, True, "la", ra, st.ANCHOR_DARK)
    st.draw_wrapped(
        d, rx + 36, ly + 145,
        "庸手输在没有常识；最厉害的人输在把“局部有效的机制”，当成了“不看边界的无敌铁律”。",
        rw - 72, "serif", 28, st.INK_LIGHT, True, 12, 4, ra, st.ANCHOR_DARK
    )
    st.draw_wrapped(
        d, rx + 36, ly + 365,
        "超过一半的大师翻车，并不是大方向错了，而是硬写死了超越年份、固定速率，或漏算了对手方的绕行与政策反制。",
        rw - 72, "sans", 23, (194, 190, 182), False, 10, 5, ra, st.ANCHOR_DARK
    )


def draw_p15(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float, data):
    hdr(d, all_done=True)
    st.draw_text(d, (st.W // 2, 132), "PROTOCOL // CONTINUOUS CALIBRATION", "mono", 17, st.TERRACOTTA, False, "mm", st.prog(t, 0.1, 0.45))
    st.draw_text(d, (st.W // 2, 178), "把 330 条历史经验，变成你的未来雷达", "serif", 50, st.INK_DARK, True, "mm", st.prog(t, 0.15, 0.55))

    cards = [
        ("01", "先查同领域底盘", "遇到任何新问题，先对照 180 条未来方向罗盘，锁定慢变量与硬约束。", st.COBALT, False),
        ("02", "再做翻车反证体检", "下判断前对照 50 条大师失手：有没有硬写年份？有没有漏算绕行与替代？", st.TERRACOTTA, True),
        ("03", "挂上领先指标追踪", "把命题放进 2026-2035 跟踪清单，按事件、机制、时间三轴每年复盘。", st.FOREST, False),
    ]
    for i, (num, hd, desc, col, dark) in enumerate(cards):
        p = st.prog(t, 0.7 + i * 1.4, 0.6)
        y = 262 + i * 176 + (1 - p) * 16
        bg_c = st.ANCHOR_DARK if dark else st.CARD_BG
        st.draw_card(d, (220, y, 1700, y + 144), fill=bg_c, outline=col if dark else st.CARD_BORDER, radius=10, alpha=p)
        d.rectangle((220, y, 226, y + 144), fill=st.fade_color(col, p))
        st.draw_text(d, (268, y + 40), num, "mono", 22, col, True, "la", p, bg_c)
        st.draw_text(d, (320, y + 34), hd, "serif", 30, st.INK_LIGHT if dark else st.INK_DARK, True, "la", p, bg_c)
        st.draw_text(d, (268, y + 88), desc, "sans", 23, (194, 190, 182) if dark else st.INK_BODY, False, "la", p, bg_c)

    st.draw_text(d, (st.W // 2, 835), "FULL COMPENDIUM // 330 ITEMS & 2026-2035 TRACKING INDICATORS IN ACCOMPANYING REPORT", "mono", 16, st.INK_MUTED, False, "mm", st.prog(t, 5.0, 0.5))


def make_paged_drawer(items_key: str, slice_start: int, slice_end: int, page_size: int, fig_prefix: str, title: str, sub_hint: str, accent_color, pill_bg, active_top: int):
    def _draw(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float, data):
        pool = data[items_key][slice_start:slice_end]
        pages = [pool[i : i + page_size] for i in range(0, len(pool), page_size)]
        n_pages = max(1, len(pages))
        page_dur = dur / n_pages
        pidx = min(n_pages - 1, int(t / page_dur))
        local_t = t - pidx * page_dur
        items = pages[pidx]

        hdr(d, active=active_top)
        rng_lbl = f"{items[0]['id']} - {items[-1]['id']}" if items else ""
        st.draw_scene_title(d, f"{fig_prefix}  //  PAGE {pidx + 1}/{n_pages} ({rng_lbl})", title, sub_hint, local_t + 2.0)

        # 右上角页码胶囊
        st.draw_pill(d, 1840, 112, f"第 {pidx + 1}/{n_pages} 页 · {rng_lbl}", accent_color, pill_bg, 19, 1.0, st.PAPER_BG)

        cw, ch, gx, gy = 860, 124, 40, 14
        sx, sy = 80, 222
        for idx, it in enumerate(items[:10]):
            col = idx % 2
            row = idx // 2
            p = st.prog(local_t, idx * 0.07, 0.36)
            x = sx + col * (cw + gx)
            y = sy + row * (ch + gy) + (1 - p) * 12
            st.draw_card(d, (x, y, x + cw, y + ch), alpha=p)
            d.rectangle((x + 12, y + 18, x + 15, y + ch - 18), fill=st.fade_color(accent_color, p, st.CARD_BG))
            st.draw_text(d, (x + 28, y + 19), it["id"], "mono", 18, accent_color, True, "la", p, st.CARD_BG)
            id_off = 96 if "-" in it["id"] else 86
            meta_txt = f"{it['s_author']}《{it['s_book']}》({it['pub_year']})"
            if len(meta_txt) > 28:
                meta_txt = meta_txt[:27] + "…"
            st.draw_text(d, (x + id_off, y + 17), meta_txt, "sans", 20, st.INK_DARK, True, "la", p, st.CARD_BG)
            st.draw_pill(d, x + cw - 16, y + 13, it["tag"], accent_color, pill_bg, 15, p, st.CARD_BG)
            st.draw_wrapped(d, x + 28, y + 54, it["claim"], cw - 48, "sans", 20, st.INK_BODY, False, 6, 2, p, st.CARD_BG)
    return _draw


SCENES = [
    {"id": "p0", "name": "P0 片头总览", "voice": st.VOICE_MALE, "draw": draw_p0,
     "narration": "欢迎来到第二部全景特辑。我们从一百三十二部著作、八千一百三十条预测里，人工淘洗去重，选出三百三十条最有含金量的预测样本：一百条封神命中、五十条最厉害的人的翻车教训，以及六大核心领域各三十条、一共一百八十条还在继续演进的未来方向。全片逐页完整展示这三百三十条预测。"},
    {"id": "p1", "name": "P1 百大精彩(1-20)：地缘与大国格局", "voice": st.VOICE_MALE,
     "narration": "先看百大精彩预测第一组，地缘政治与国际秩序，第一号到第二十号。麦金德在一九一九年看准铁路和航空将打开心脏地带；扎卡利亚在二零零八年精准拆解后美国世界的分层权力；卡普兰提前十年指出欧亚大陆边缘地带的战略博弈将重燃；李光耀早年就指出缺少统一财政支撑的欧元区必然承受长期摩擦。",
     "draw": make_paged_drawer("part_a", 0, 20, 10, "SECTION 01 // TOP 100 HITS", "百大精彩预测 (1-20)：地缘与大国格局", "地理边界、海陆通道与大国利益约束，是长周期最稳的地缘锚", st.FOREST, st.FOREST_BG, 1)},
    {"id": "p2", "name": "P2 百大精彩(21-40)：金融与能源硬账本", "voice": st.VOICE_FEMALE,
     "narration": "第二组，第二十一号到第四十号，宏观金融、人口与能源生态。杰文斯在一八六六年用煤矿开采成本账本算出英国煤耗增速无法维持；塔勒布在《黑天鹅》中一针见血指出银行盈利归私人、爆雷由央行和纳税人兜底；达利欧看准严重去杠杆必走向央行货币化；国际能源署则通过分矿种产能账本拿下高胜率。",
     "draw": make_paged_drawer("part_a", 20, 40, 10, "SECTION 01 // TOP 100 HITS", "百大精彩预测 (21-40)：金融与能源硬账本", "算清谁买单、存量边界与矿山产能，远胜宏观拍点位", st.FOREST, st.FOREST_BG, 1)},
    {"id": "p3", "name": "P3 百大精彩(41-60)：科技商业与产业颠覆", "voice": st.VOICE_MALE,
     "narration": "第三组，第四十一号到第六十号，科技商业与产业颠覆。克里斯坦森用价值网约束，准确预言在位巨头会在闪存和电动车浪潮里反应迟钝；弗里德曼在二零零五年看准非西方软件与数字平台崛起；英国政府科学办公室二零零六年的智能基础设施报告，历经二十年严格胜率超过七成；凯文·凯利《失控》预见了分布式网络与合成生物学兴起。",
     "draw": make_paged_drawer("part_a", 40, 60, 10, "SECTION 01 // TOP 100 HITS", "百大精彩预测 (41-60)：科技商业与产业颠覆", "在位者的利润包袱与基础设施升级周期，决定谁会被颠覆", st.FOREST, st.FOREST_BG, 1)},
    {"id": "p4", "name": "P4 百大精彩(61-80)：AI演进与社会制度", "voice": st.VOICE_FEMALE,
     "narration": "第四组，第六十一号到第八十号，人工智能前沿、语言变迁与社会制度。博斯特罗姆在二零一四年就指出对齐与控制难题会随算力和算法同步放大；美国国家科技委与斯坦福百年报告看准了无人机商业化落地；大卫·格拉多尔精准抓住英语全球通用语的协调网络地位；世界银行用人口结构拆解了高收入国家靠补贴极难逆转少子化。",
     "draw": make_paged_drawer("part_a", 60, 80, 10, "SECTION 01 // TOP 100 HITS", "百大精彩预测 (61-80)：AI 演进与社会制度", "模型能力、社会协调网络与人口年龄底座决定了结构惯性", st.FOREST, st.FOREST_BG, 1)},
    {"id": "p5", "name": "P5 百大精彩(81-100)：跨世纪工程功能预见", "voice": st.VOICE_MALE,
     "narration": "第五组，第八十一号到第一百号，跨世纪工程功能预见。令人惊叹的是，凡尔纳在一八六三年写下电算机与传真；威尔斯在一九零一年精准推演出轻便公路内燃机、郊区通勤扩张和空中力量打破战壕僵局；戴维在一九一九年看准跨洋航空邮件普及；霍尔丹在一九二四年预见到风能制氢与储能电网。他们赢在推演工程功能，而不是猜政治终局。",
     "draw": make_paged_drawer("part_a", 80, 100, 10, "SECTION 01 // TOP 100 HITS", "百大精彩预测 (81-100)：跨世纪工程功能预见", "沿着工程雏形与成本下降链条推演功能扩散，百年后依然惊艳", st.FOREST, st.FOREST_BG, 1)},
    {"id": "p6", "name": "P6 五十高手翻车总纲", "voice": st.VOICE_FEMALE, "draw": draw_p6,
     "narration": "看完一百个高光时刻，我们更要看最厉害的人是怎么错的。我们从四十六部顶尖智库和名家代表作里，挑出了最具代表性的五十条错误。统计显示：超过一半的翻车不是大方向错，而是把方向偷换成硬年份或极端量词；其次是忽略了对手方的绕行与政策反制，以及低估替代供给与技术跃迁。"},
    {"id": "p7", "name": "P7 高手翻车(1-25)：机构、地缘与宏观名家", "voice": st.VOICE_MALE,
     "narration": "看前二十五条高手翻车。即便是国际能源署，也低估了中国与印尼产能对俄罗斯镍禁令的库存对冲；鲁比尼在二零二二年押注比七十年代更糟的滞胀，结果随后通胀回落；李光耀与布热津斯基用上一代领导人的克制惯性外推中国外交姿态，结果被现实证伪；凯恩斯在一九一九年漏算了美洲小麦产区的快速替代。",
     "draw": make_paged_drawer("part_b", 0, 25, 10, "SECTION 02 // TOP 50 MASTER MISSES", "高手翻车榜 (1-25)：机构、地缘与宏观名家", "重点复盘：惯性外推、忽略替代产区与高估政策摩擦", st.TERRACOTTA, st.TERRACOTTA_BG, 2)},
    {"id": "p8", "name": "P8 高手翻车(26-50)：科技泰斗与经典失手", "voice": st.VOICE_FEMALE,
     "narration": "再看后二十五条大师翻车。克里斯坦森虽然看对了传统车企迟钝，却押错电动车会像低端颠覆一样先从廉价简陋切入，忽略了特斯拉靠高性能破局；凯文·凯利预测二零二六年谷歌主营不再是搜索；彼得·蒂尔误判计算机几乎不与人类争夺电力资源；英国科学办公室写死二零一五年金砖四国经济总量超美国，结果直接翻车。",
     "draw": make_paged_drawer("part_b", 25, 50, 10, "SECTION 02 // TOP 50 MASTER MISSES", "高手翻车榜 (26-50)：科技泰斗与经典失手", "重点复盘：写死超越年份、错判破局维度、漏算算力抢电", st.TERRACOTTA, st.TERRACOTTA_BG, 2)},
    {"id": "p9", "name": "P9 未来方向①：地缘政治与国际秩序(30条)", "voice": st.VOICE_MALE,
     "narration": "下面进入未来方向罗盘，六个领域各三十条，帮你接着往后看。第一领域：地缘政治与国际秩序。核心主线三条：一是多极碎片化与非西方人口体量上升，但美国在军事和创新底盘上短期不会瞬间崩塌；二是欧亚边缘带、印太海域和关键海峡摩擦长期存在；三是盟友防务分担、区域安全架构和供应链绕行继续加速。接着看，重点盯军费占GDP比重和转口贸易份额。",
     "draw": make_paged_drawer("part_c", 0, 30, 10, "SECTION 03 // FUTURE COMPASS 01", "未来方向罗盘 ①：地缘政治与国际秩序（30 条）", "跟踪指标：大国军费占比 · 关键海峡航运保费 · 供应链友岸转口份额", st.COBALT, st.COBALT_BG, 3)},
    {"id": "p10", "name": "P10 未来方向②：宏观经济、金融与市场(30条)", "voice": st.VOICE_FEMALE,
     "narration": "第二领域：宏观经济、金融与市场三十条。核心主线三条：一是在高主权债务与财政赤字约束下，财政主导和央行隐性兜底成为常态；二是人口老龄化拖累多国长期潜在增速，而能源转型与供应链重塑抬升通胀中枢波动；三是中等收入国家在研发和制度门槛上面临剧烈分化。接着看，重点盯主权债利息占财政收入比和全要素生产率。",
     "draw": make_paged_drawer("part_c", 30, 60, 10, "SECTION 03 // FUTURE COMPASS 02", "未来方向罗盘 ②：宏观经济、金融与市场（30 条）", "跟踪指标：主权债利息/财政收入比 · 实际利率 · 全要素生产率(TFP)", st.COBALT, st.COBALT_BG, 3)},
    {"id": "p11", "name": "P11 未来方向③：科技、商业与产业颠覆(30条)", "voice": st.VOICE_MALE,
     "narration": "第三领域：科技、商业与产业颠覆三十条。核心主线三条：一是交通和能源等物理基础设施全面数字化，带来效率同时放大网络安全脆弱性；二是制造业加速向软件定义、服务化和自动化演进；三是平台巨头与开源生态、反垄断监管之间的拉锯战长期持续。接着看，重点盯工业机器人密度、服务营收占比和在位者毛利包袱。",
     "draw": make_paged_drawer("part_c", 60, 90, 10, "SECTION 03 // FUTURE COMPASS 03", "未来方向罗盘 ③：科技、商业与产业颠覆（30 条）", "跟踪指标：服务化毛利占比 · 电池与算力单位成本 · 反垄断与开源份额", st.COBALT, st.COBALT_BG, 3)},
    {"id": "p12", "name": "P12 未来方向④：AI与奇点前沿(30条)", "voice": st.VOICE_FEMALE,
     "narration": "第四领域：人工智能与奇点前沿三十条。核心主线三条：一是通用能力继续沿着算力与算法积累推进，但在科研代码突破的同时仍呈现明显的能力参差；二是大规模训练和推理越来越受制于电力、变电设备和电网接入排队；三是模型对齐失控风险与各国主权AI安全监管同步升温。接着看，重点盯企业真实工作流付费留存率和电网审批周期。",
     "draw": make_paged_drawer("part_c", 90, 120, 10, "SECTION 03 // FUTURE COMPASS 04", "未来方向罗盘 ④：AI 与奇点前沿（30 条）", "跟踪指标：企业工作流真实付费率 · 电网接入队列 · 红队安全基准", st.TERRACOTTA, st.TERRACOTTA_BG, 3)},
    {"id": "p13", "name": "P13 未来方向⑤：人口、能源、资源与生态(30条)", "voice": st.VOICE_MALE,
     "narration": "第五领域：人口、能源、资源与生态三十条。核心主线三条：一是数据中心用电翻倍与电气化推高总电力需求，电网和储能成为比发电装机更硬的瓶颈；二是铜锂等关键矿产精炼高度集中，高价正倒逼磷酸铁锂和钠离子等替代路线；三是东亚和欧洲深度老龄化几乎不可逆，跨国移民与养老财政压力持续外溢。接着看，盯在建矿山资本开支和分年龄段劳动参与率。",
     "draw": make_paged_drawer("part_c", 120, 150, 10, "SECTION 03 // FUTURE COMPASS 05", "未来方向罗盘 ⑤：人口、能源、资源与生态（30 条）", "跟踪指标：电网储能配套比 · 关键矿产精炼CR3 · 20-39岁人口基数", st.FOREST, st.FOREST_BG, 3)},
    {"id": "p14", "name": "P14 未来方向⑥：社会结构、制度、文化与教育(30条)", "voice": st.VOICE_FEMALE,
     "narration": "第六领域：社会结构、制度、文化与教育三十条。核心主线三条：一是人工智能与远程协作重塑白领技能溢价，学校教育从知识灌输转向终身微证书与能力分层；二是算法舆论场与技术官僚治理放大民主制度极化与公共信任摩擦；三是英语仍稳居国际通用语核心，但多语数字本地化并行。接着看，盯大学毕业生工资溢价和社会信任民调。",
     "draw": make_paged_drawer("part_c", 150, 180, 10, "SECTION 03 // FUTURE COMPASS 06", "未来方向罗盘 ⑥：社会结构、制度、文化与教育（30 条）", "跟踪指标：大学工资溢价 · 职业微证书注册比 · 公共财政社保承压比", st.AMBER, st.AMBER_BG, 3)},
    {"id": "p15", "name": "P15 总结：把330条经验变成未来雷达", "voice": st.VOICE_MALE, "draw": draw_p15,
     "narration": "最后记住三步用法：第一，遇到新问题，先查一百八十条同领域未来方向，看清慢变量和硬约束；第二，自己下判断前，拿五十条大师翻车清单做一次反证体检；第三，挂上领先指标，按事件、机制、时间三轴每年复盘。全部三百三十条明细与跟踪指标已为你整理成全集文档，随时查阅。"},
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", help="只重渲染指定场景 id")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)
    data = json.loads(CURATED_JSON.read_text(encoding="utf-8"))

    meta_file = SCRATCH_DIR / "meta.json"
    meta_by_id = {}
    if args.scene and meta_file.exists():
        for m in json.loads(meta_file.read_text(encoding="utf-8")):
            meta_by_id[m["id"]] = m

    mp4s, new_meta = [], []
    for sc in SCENES:
        sid = sc["id"]
        out_mp4 = SCRATCH_DIR / f"{sid}.mp4"
        if args.scene and sid != args.scene and out_mp4.exists() and sid in meta_by_id:
            mp4s.append(out_mp4)
            new_meta.append(meta_by_id[sid])
            continue
        wav_path, adur, dur, subs = st.prepare_neural_audio(sc, SCRATCH_DIR, rate="+5%")
        st.render_scene_pipeline(sc, wav_path, dur, subs, sc["draw"], SCRATCH_DIR, data=data)
        actual_dur = st.ffprobe_duration(out_mp4)
        mp4s.append(out_mp4)
        new_meta.append({
            "id": sid, "name": sc["name"], "voice": sc["voice"],
            "audio_dur": adur, "target_dur": dur, "actual_dur": actual_dur, "subs": subs,
        })

    st.concat_all(mp4s, OUT_MP4, SCRATCH_DIR)
    st.write_srt_and_meta(new_meta, OUT_SRT, SCRATCH_DIR)
    print(f"DONE: {OUT_MP4} ({st.ffprobe_duration(OUT_MP4):.2f}s), {OUT_SRT}")


if __name__ == "__main__":
    main()
