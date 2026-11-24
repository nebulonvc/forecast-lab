#!/usr/bin/env python3
"""
《手把手学预测》Anthropic x Kimi 科研档案风 + 双人神经网络中文配音版
输出:
  - media/videos/01-hands-on-forecasting-tutorial.mp4
  - media/subtitles/01-hands-on-forecasting-tutorial.srt
"""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw

import sci_theme as st

BASE_DIR = Path(__file__).resolve().parent.parent
OUT_MP4 = BASE_DIR / "videos/01-hands-on-forecasting-tutorial.mp4"
OUT_SRT = BASE_DIR / "subtitles/01-hands-on-forecasting-tutorial.srt"
SCRATCH_DIR = BASE_DIR / ".build_cache/part1"

STEPS = ["拆题", "选老师", "算账", "分支", "定硬度", "扫雷", "复盘"]
ARCHIVE = "FORECAST-LAB // ARCHIVE N = 8,130"


def hdr(d, active=-1, all_done=False):
    st.draw_header(d, ARCHIVE, STEPS, active_idx=active, all_done=all_done)


def draw_s0(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=-1)
    a0 = st.prog(t, 0.1, 0.55)
    a1 = st.prog(t, 0.25, 0.65)
    a2 = st.prog(t, 0.65, 0.65)
    st.draw_text(d, (st.W // 2, 165 + (1 - a0) * 14), "EMPIRICAL FORECASTING PROTOCOL // 1531 - 2026", "mono", 18, st.TERRACOTTA, False, "mm", a0)
    st.draw_text(d, (st.W // 2, 248 + (1 - a1) * 20), "手把手学预测", "serif", 88, st.INK_DARK, True, "mm", a1)
    st.draw_text(d, (st.W // 2, 336 + (1 - a2) * 16), "向 132 部著作里最准的那批人学习", "sans", 32, st.COBALT, True, "mm", a2)
    lp = st.prog(t, 0.5, 0.7)
    d.line([(st.W // 2 - int(320 * lp), 385), (st.W // 2 + int(320 * lp), 385)], fill=st.CARD_BORDER, width=1)

    cards = [
        ("FIG. A", 132, "部独立著作", "覆盖近五百年跨学科预测文献", 1.2, st.COBALT, False),
        ("FIG. B", 8130, "条可评分预测", "全部从原书逐句抽取与界定", 2.0, st.TERRACOTTA, False),
        ("FIG. C", 5060, "条已明确判定", "经公开统计与历史事实核验", 2.8, st.FOREST, True),
    ]
    cw, ch, gap = 460, 265, 50
    sx = (st.W - (3 * cw + 2 * gap)) // 2
    cy = 435
    for i, (fig_k, target, unit, desc, st_t, col, dark) in enumerate(cards):
        p = st.prog(t, st_t, 0.75)
        if p <= 0.01:
            continue
        x = sx + i * (cw + gap)
        y = cy + (1 - p) * 24
        bg_c = st.ANCHOR_DARK if dark else st.CARD_BG
        bd_c = st.ANCHOR_DARK if dark else st.CARD_BORDER
        st.draw_card(d, (x, y, x + cw, y + ch), fill=bg_c, outline=bd_c, radius=10, width=1, alpha=p)
        d.rectangle((x, y, x + cw, y + 4), fill=st.fade_color(col, p))
        st.draw_text(d, (x + 28, y + 26), fig_k, "mono", 15, col if dark else st.INK_MUTED, False, "la", p, bg_c)
        cp = st.prog(t, st_t + 0.1, 1.2)
        val = int(round(target * cp))
        vstr = f"{val:,}" if target >= 1000 else str(val)
        st.draw_text(d, (x + cw // 2, y + 108), vstr, "mono", 66, col if not dark else st.INK_LIGHT, True, "mm", p, bg_c)
        st.draw_text(d, (x + cw // 2, y + 174), unit, "serif", 28, st.INK_LIGHT if dark else st.INK_DARK, True, "mm", p, bg_c)
        st.draw_text(d, (x + cw // 2, y + 224), desc, "sans", 19, (190, 186, 178) if dark else st.INK_MUTED, False, "mm", p, bg_c)

    ab = st.prog(t, 4.4, 0.6)
    st.draw_text(d, (st.W // 2, 775), "7 个可落地步骤  ·  6 大领域老师  ·  5 大高发翻车雷区", "sans", 24, st.INK_MUTED, False, "mm", ab)


def draw_s1(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=-1)
    st.draw_scene_title(d, "FIG. 01  //  BASELINE PERFORMANCE BY ARCHETYPE", "成绩单：全库没有“全能先知”", "按六类作者群体统计：严格胜率（绿） vs 错误率（赤陶）", t)

    groups = [
        ("国际机构与政府智库", 47.0, 6.3),
        ("地缘与社科政治学者", 34.3, 11.7),
        ("政治家与战略实务者", 33.1, 8.5),
        ("经济学家与金融投资人", 30.3, 13.9),
        ("古典思想家与科幻/乌托邦作家", 29.6, 31.3),
        ("科技商业思想家与产业实践者", 28.8, 10.8),
    ]
    lx, lw, ty = 80, 1160, 224
    st.draw_card(d, (lx, ty, lx + lw, 895), alpha=st.prog(t, 0.2, 0.5))

    la = st.prog(t, 0.4, 0.4)
    d.rectangle((lx + 36, ty + 28, lx + 60, ty + 42), fill=st.fade_color(st.FOREST, la, st.CARD_BG))
    st.draw_text(d, (lx + 70, ty + 35), "严格胜率", "sans", 20, st.INK_DARK, True, "lm", la, st.CARD_BG)
    d.rectangle((lx + 190, ty + 31, lx + 214, ty + 39), fill=st.fade_color(st.TERRACOTTA, la, st.CARD_BG))
    st.draw_text(d, (lx + 224, ty + 35), "错误率", "sans", 20, st.INK_DARK, True, "lm", la, st.CARD_BG)
    st.draw_text(d, (lx + lw - 36, ty + 35), "全库均值: 严格 33.3%", "sans", 18, st.INK_MUTED, False, "rm", la, st.CARD_BG)

    bar_x = lx + 395
    max_bw = 580
    # 均值虚线 (33.3%)
    mean_x = bar_x + int((33.3 / 55.0) * max_bw)
    st.draw_dashed_line(d, (mean_x, ty + 68), (mean_x, 875), fill=st.REG_MARK, width=1)

    for i, (name, sv, ev) in enumerate(groups):
        st_t = 0.7 + i * 0.65
        p = st.prog(t, st_t, 0.55)
        bp = st.prog(t, st_t + 0.1, 0.85)
        y = ty + 84 + i * 98
        st.draw_text(d, (bar_x - 22, y + 24), name, "sans", 22, st.INK_DARK if i == 0 else st.INK_BODY, i == 0, "rm", p, st.CARD_BG)
        gw = max(2, int((sv / 55.0) * max_bw * bp))
        d.rectangle((bar_x, y + 4, bar_x + gw, y + 28), fill=st.fade_color(st.FOREST, p, st.CARD_BG))
        st.draw_text(d, (bar_x + gw + 12, y + 16), f"{sv * bp:.1f}%", "mono", 21, st.FOREST, True, "lm", p, st.CARD_BG)
        rw = max(2, int((ev / 55.0) * max_bw * bp))
        d.rectangle((bar_x, y + 36, bar_x + rw, y + 47), fill=st.fade_color(st.TERRACOTTA, p, st.CARD_BG))
        st.draw_text(d, (bar_x + rw + 12, y + 41), f"错 {ev * bp:.1f}%", "sans", 18, st.TERRACOTTA, ev > 20, "lm", p, st.CARD_BG)

    # 右侧深色档案对照卡
    rx, rw = 1280, 560
    ra = st.prog(t, 7.2, 0.65)
    st.draw_card(d, (rx, ty, rx + rw, 895), fill=st.ANCHOR_DARK, outline=st.ANCHOR_DARK, alpha=ra)
    st.draw_text(d, (rx + 36, ty + 34), "CASE CONTRAST // H. G. WELLS", "mono", 15, st.TERRACOTTA, False, "la", ra, st.ANCHOR_DARK)
    st.draw_text(d, (rx + 36, ty + 62), "同一个作者，换领域也会塌", "serif", 28, st.INK_LIGHT, True, "la", ra, st.ANCHOR_DARK)

    ra1 = st.prog(t, 8.0, 0.6)
    st.draw_card(d, (rx + 32, 338 + (1 - ra1) * 16, rx + rw - 32, 520 + (1 - ra1) * 16), fill=(35, 42, 38), outline=st.FOREST, width=1, alpha=ra1, bg=st.ANCHOR_DARK)
    st.draw_text(d, (rx + 56, 366 + (1 - ra1) * 16), "H. G. 威尔斯《预言》(1901)", "sans", 24, st.INK_LIGHT, True, "la", ra1, (35, 42, 38))
    st.draw_text(d, (rx + 56, 408 + (1 - ra1) * 16), "基于工程雏形做功能扩散推演", "sans", 19, (186, 184, 178), False, "la", ra1, (35, 42, 38))
    st.draw_text(d, (rx + 56, 456 + (1 - ra1) * 16), "严格胜率", "sans", 22, (160, 200, 176), True, "la", ra1, (35, 42, 38))
    st.draw_text(d, (rx + 170, 448 + (1 - ra1) * 16), "52.2%", "mono", 38, (118, 198, 152), True, "la", ra1, (35, 42, 38))

    ra_arr = st.prog(t, 9.0, 0.45)
    st.draw_arrow_aa(img, (rx + rw // 2, 535), (rx + rw // 2, 602), color=st.TERRACOTTA, width=3, head=12, alpha=ra_arr)

    ra2 = st.prog(t, 9.4, 0.6)
    st.draw_card(d, (rx + 32, 616 + (1 - ra2) * 16, rx + rw - 32, 800 + (1 - ra2) * 16), fill=(48, 30, 28), outline=st.TERRACOTTA, width=1, alpha=ra2, bg=st.ANCHOR_DARK)
    st.draw_text(d, (rx + 56, 644 + (1 - ra2) * 16), "H. G. 威尔斯《公开的阴谋》(1928)", "sans", 24, st.INK_LIGHT, True, "la", ra2, (48, 30, 28))
    st.draw_text(d, (rx + 56, 686 + (1 - ra2) * 16), "脱离工程约束，空想世界政府终局", "sans", 19, (186, 184, 178), False, "la", ra2, (48, 30, 28))
    st.draw_text(d, (rx + 56, 734 + (1 - ra2) * 16), "错误率飙升至", "sans", 22, (235, 148, 126), True, "la", ra2, (48, 30, 28))
    st.draw_text(d, (rx + 215, 726 + (1 - ra2) * 16), "40.9%", "mono", 38, (242, 128, 98), True, "la", ra2, (48, 30, 28))


def draw_s2(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=-1)
    st.draw_scene_title(d, "FIG. 02  //  HORIZON DIFFICULTY CURVE", "底线：时间越远，预测越难", "按“截止年 - 写作/出版年”分档的误差上升与方向命中衰减", t)

    gx, gy, gw, gh = 80, 222, 1760, 385
    ga = st.prog(t, 0.2, 0.45)
    st.draw_card(d, (gx, gy, gx + gw, gy + gh), alpha=ga)

    d.line([(gx + 52, gy + 34), (gx + 100, gy + 34)], fill=st.fade_color(st.TERRACOTTA, ga, st.CARD_BG), width=4)
    st.draw_text(d, (gx + 112, gy + 34), "错误率 (%)", "sans", 20, st.TERRACOTTA, True, "lm", ga, st.CARD_BG)
    d.line([(gx + 260, gy + 34), (gx + 308, gy + 34)], fill=st.fade_color(st.COBALT, ga, st.CARD_BG), width=4)
    st.draw_text(d, (gx + 320, gy + 34), "方向命中率 (%)", "sans", 20, st.COBALT, True, "lm", ga, st.CARD_BG)

    tiers = ["0-3年", "4-9年", "10-19年", "20-39年", "40-99年", ">=100年"]
    errs = [2.9, 5.2, 8.6, 10.1, 39.9, 25.6]
    dirs = [81.0, 57.6, 60.3, 52.6, 27.7, 37.9]
    px0, px1, py0, py1 = gx + 140, gx + gw - 120, gy + 320, gy + 82

    for val in (0, 20, 40, 60, 80):
        yy = py0 - (val / 90.0) * (py0 - py1)
        st.draw_dashed_line(d, (px0 - 15, yy), (px1 + 15, yy), fill=st.GRID_LINE, width=1)
        st.draw_text(d, (px0 - 26, yy), f"{val}%", "mono", 16, st.INK_MUTED, False, "rm", ga, st.CARD_BG)

    pts_e = [(px0 + i * (px1 - px0) / 5.0, py0 - (errs[i] / 90.0) * (py0 - py1)) for i in range(6)]
    pts_d = [(px0 + i * (px1 - px0) / 5.0, py0 - (dirs[i] / 90.0) * (py0 - py1)) for i in range(6)]
    for i in range(6):
        st.draw_text(d, (pts_d[i][0], py0 + 28), tiers[i], "sans", 20, st.INK_DARK, True, "mm", ga, st.CARD_BG)

    lp = st.prog(t, 0.9, 4.2)
    cur_seg = lp * 5.0
    vis_d, vis_e = [pts_d[0]], [pts_e[0]]
    for i in range(5):
        sp = st.clamp(cur_seg - i, 0.0, 1.0)
        if sp <= 0:
            break
        vis_d.append((pts_d[i][0] + (pts_d[i + 1][0] - pts_d[i][0]) * sp, pts_d[i][1] + (pts_d[i + 1][1] - pts_d[i][1]) * sp))
        vis_e.append((pts_e[i][0] + (pts_e[i + 1][0] - pts_e[i][0]) * sp, pts_e[i][1] + (pts_e[i + 1][1] - pts_e[i][1]) * sp))
    st.draw_polyline_aa(img, vis_d, st.COBALT, 4)
    st.draw_polyline_aa(img, vis_e, st.TERRACOTTA, 4)

    for i in range(6):
        pa = st.prog(t, 0.9 + i * 0.68, 0.38)
        if pa > 0.05:
            dx, dy = pts_d[i]
            ex, ey = pts_e[i]
            d.ellipse((dx - 6, dy - 6, dx + 6, dy + 6), fill=st.CARD_BG, outline=st.fade_color(st.COBALT, pa, st.CARD_BG), width=3)
            st.draw_text(d, (dx, dy + (24 if i == 4 else -20)), f"{dirs[i]:.1f}%", "mono", 18, st.COBALT, True, "mm", pa, st.CARD_BG)
            d.ellipse((ex - 6, ey - 6, ex + 6, ey + 6), fill=st.CARD_BG, outline=st.fade_color(st.TERRACOTTA, pa, st.CARD_BG), width=3)
            st.draw_text(d, (ex, ey + (24 if i == 5 else -20)), f"{errs[i]:.1f}%", "mono", 18, st.TERRACOTTA, True, "mm", pa, st.CARD_BG)

    c1a = st.prog(t, 6.0, 0.6)
    c2a = st.prog(t, 7.8, 0.6)
    cw, cy, ch = 860, 628, 195
    st.draw_card(d, (80, cy + (1 - c1a) * 16, 80 + cw, cy + ch + (1 - c1a) * 16), alpha=c1a)
    d.rectangle((80, cy + (1 - c1a) * 16, 80 + cw, cy + 4 + (1 - c1a) * 16), fill=st.fade_color(st.AMBER, c1a))
    st.draw_text(d, (114, cy + 28 + (1 - c1a) * 16), "库兹韦尔《奇点更近》(2024 · 窗口 2 年)", "serif", 26, st.INK_DARK, True, "la", c1a, st.CARD_BG)
    st.draw_text(d, (114, cy + 78 + (1 - c1a) * 16), "89.8%", "mono", 40, st.AMBER, True, "la", c1a, st.CARD_BG)
    st.draw_text(d, (256, cy + 84 + (1 - c1a) * 16), "尚未到期", "sans", 28, st.AMBER, True, "la", c1a, st.CARD_BG)
    st.draw_text(d, (114, cy + 142 + (1 - c1a) * 16), "短窗里仅 24 条近期已兑现变化，不能提前加冕", "sans", 20, st.INK_MUTED, False, "la", c1a, st.CARD_BG)

    st.draw_card(d, (980, cy + (1 - c2a) * 16, 980 + cw, cy + ch + (1 - c2a) * 16), fill=st.ANCHOR_DARK, outline=st.ANCHOR_DARK, alpha=c2a)
    d.rectangle((980, cy + (1 - c2a) * 16, 980 + cw, cy + 4 + (1 - c2a) * 16), fill=st.fade_color(st.TERRACOTTA, c2a))
    st.draw_text(d, (1014, cy + 28 + (1 - c2a) * 16), "库兹韦尔《奇点临近》(2005 · 窗口 21 年)", "serif", 26, st.INK_LIGHT, True, "la", c2a, st.ANCHOR_DARK)
    st.draw_text(d, (1014, cy + 84 + (1 - c2a) * 16), "严格", "sans", 24, (200, 196, 188), True, "la", c2a, st.ANCHOR_DARK)
    st.draw_text(d, (1076, cy + 78 + (1 - c2a) * 16), "5.4%", "mono", 38, st.TERRACOTTA, True, "la", c2a, st.ANCHOR_DARK)
    st.draw_text(d, (1210, cy + 84 + (1 - c2a) * 16), "错误", "sans", 24, (200, 196, 188), True, "la", c2a, st.ANCHOR_DARK)
    st.draw_text(d, (1272, cy + 78 + (1 - c2a) * 16), "27.0%", "mono", 38, st.TERRACOTTA, True, "la", c2a, st.ANCHOR_DARK)
    st.draw_text(d, (1014, cy + 142 + (1 - c2a) * 16), "经过完整二十年结算，硬时间节点大量落空", "sans", 20, (186, 184, 178), False, "la", c2a, st.ANCHOR_DARK)

    ba = st.prog(t, 10.2, 0.5)
    st.draw_card(d, (480, 845, 1440, 900), fill=st.COBALT_BG, outline=st.COBALT, width=1, alpha=ba)
    st.draw_text(d, (st.W // 2, 872), "铁律：只和同样时间跨度的人比", "serif", 26, st.COBALT, True, "mm", ba, st.COBALT_BG)


def draw_s3(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=0)
    st.draw_scene_title(d, "STEP 01 // CLAIM DECOMPOSITION", "第一步：把大判断拆成可检验的命题", "模糊口号无法计分，拆成 6 要素才能进入实证核验", t)

    a0 = st.prog(t, 0.4, 0.45)
    st.draw_card(d, (540, 220 + (1 - a0) * 12, 1380, 290 + (1 - a0) * 12), fill=st.AMBER_BG, outline=st.AMBER, radius=8, alpha=a0)
    st.draw_text(d, (st.W // 2, 255 + (1 - a0) * 12), "模糊说法：“AI 会取代大量工作”", "sans", 26, st.AMBER, True, "mm", a0, st.AMBER_BG)

    blocks = [
        ("01", "主体", st.COBALT, st.COBALT_BG),
        ("02", "对象", st.FOREST, st.FOREST_BG),
        ("03", "量词", st.AMBER, st.AMBER_BG),
        ("04", "指标", st.INK_DARK, (236, 234, 226)),
        ("05", "期限", st.COBALT, st.COBALT_BG),
        ("06", "条件", st.TERRACOTTA, st.TERRACOTTA_BG),
    ]
    bw, bh, gap = 240, 88, 32
    sx = (st.W - (6 * bw + 5 * gap)) // 2
    for i, (num, lbl, col, bgc) in enumerate(blocks):
        p = st.prog(t, 1.5 + i * 0.42, 0.42)
        x = sx + i * (bw + gap)
        y = 330 + (1 - p) * 18
        st.draw_card(d, (x, y, x + bw, y + bh), fill=bgc, outline=col, width=1, alpha=p)
        st.draw_text(d, (x + 20, y + 18), num, "mono", 16, col, True, "la", p, bgc)
        st.draw_text(d, (x + bw // 2, y + 54), lbl, "serif", 28, col, True, "mm", p, bgc)

    sa = st.prog(t, 4.8, 0.65)
    st.draw_card(d, (80, 458 + (1 - sa) * 16, 1840, 668 + (1 - sa) * 16), alpha=sa)
    st.draw_text(d, (124, 492 + (1 - sa) * 16), "OPERATIONALIZED CLAIM // 可检验改写：", "mono", 16, st.INK_MUTED, False, "la", sa, st.CARD_BG)

    segs = [
        ("若无大规模监管，", st.TERRACOTTA, "条件"),
        ("到 2030 年，", st.COBALT, "期限"),
        ("美国", st.COBALT, "主体"),
        ("白领岗位数", st.INK_DARK, "指标"),
        ("比 2025 年", st.FOREST, "对象"),
        ("下降 >= 10%", st.AMBER, "量词"),
    ]
    cx = 124
    sy = 548 + (1 - sa) * 16
    for txt, col, tag in segs:
        tw = st.text_width(txt, "sans", 32, True)
        st.draw_text(d, (cx, sy), txt, "sans", 32, col, True, "la", sa, st.CARD_BG)
        st.draw_text(d, (cx + tw / 2, sy + 50), f"[{tag}]", "sans", 18, st.INK_MUTED, False, "mm", sa, st.CARD_BG)
        cx += tw + 12

    ladder = ["出现", "普及", "主导", "取代"]
    lw, lh, lgap = 250, 74, 110
    lx0 = (st.W - (4 * lw + 3 * lgap)) // 2
    for i, word in enumerate(ladder):
        lp = st.prog(t, 8.8 + i * 0.7, 0.45)
        x = lx0 + i * (lw + lgap)
        y = 740 + (1 - lp) * 14
        st.draw_card(d, (x, y, x + lw, y + lh), fill=st.ANCHOR_DARK, outline=st.ANCHOR_DARK, alpha=lp)
        st.draw_text(d, (x + lw // 2, y + lh // 2), word, "serif", 30, st.INK_LIGHT, True, "mm", lp, st.ANCHOR_DARK)
        if i < 3:
            np = st.prog(t, 9.2 + i * 0.7, 0.35)
            st.draw_text(d, (x + lw + lgap // 2, y + lh // 2), "!=", "mono", 30, st.TERRACOTTA, True, "mm", np)


def draw_s4(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=1)
    st.draw_scene_title(d, "STEP 02 // DOMAIN-SPECIFIC LENSES", "第二步：按领域选对老师", "没有通用大师，不同领域盯住的硬约束截然不同", t)

    cards = [
        ("01", "地缘政治", "扎卡利亚 · 卡普兰 · 李光耀", "地理底盘 ＋ 大国利益约束", st.COBALT, st.COBALT_BG, ""),
        ("02", "宏观金融", "达利欧《债务危机》· 塔勒布", "债务机制 ＋ 风险不对称", st.TERRACOTTA, st.TERRACOTTA_BG, "别押点位"),
        ("03", "产业颠覆", "克里斯坦森《创新者的窘境》", "价值网 ＋ 在位者利润包袱", st.FOREST, st.FOREST_BG, ""),
        ("04", "人工智能", "博斯特罗姆 ＋ IEA", "条件判断 ＋ 算力电力账本", st.COBALT, st.COBALT_BG, ""),
        ("05", "能源资源", "国际能源署(IEA) · 杰文斯", "分矿种 · 分在建产能算账", st.FOREST, st.FOREST_BG, ""),
        ("06", "社会制度", "埃德蒙·伯克《法国革命论》", "财政 · 军纪 · 产权 · 秩序", st.AMBER, st.AMBER_BG, ""),
    ]
    cw, ch, gx, gy = 560, 300, 40, 32
    sx = (st.W - (3 * cw + 2 * gx)) // 2
    sy = 232
    for i, (num, dom, teacher, focus, col, bgc, badge) in enumerate(cards):
        p = st.prog(t, 0.7 + i * 2.1, 0.55)
        x = sx + (i % 3) * (cw + gx)
        y = sy + (i // 3) * (ch + gy) + (1 - p) * 20
        st.draw_card(d, (x, y, x + cw, y + ch), alpha=p)
        d.rectangle((x, y, x + cw, y + 4), fill=st.fade_color(col, p))
        st.draw_text(d, (x + 26, y + 26), num, "mono", 16, col, True, "la", p, st.CARD_BG)
        st.draw_text(d, (x + 64, y + 22), dom, "serif", 28, st.INK_DARK, True, "la", p, st.CARD_BG)
        if badge:
            st.draw_pill(d, x + cw - 20, y + 20, badge, st.TERRACOTTA, st.TERRACOTTA_BG, 16, p, st.CARD_BG)
        d.line([(x + 24, y + 70), (x + cw - 24, y + 70)], fill=st.fade_color(st.GRID_LINE, p, st.CARD_BG), width=1)
        st.draw_text(d, (x + 26, y + 92), "代表老师", "sans", 17, st.INK_MUTED, False, "la", p, st.CARD_BG)
        st.draw_text(d, (x + 26, y + 122), teacher, "sans", 24, st.INK_DARK, True, "la", p, st.CARD_BG)
        st.draw_text(d, (x + 26, y + 184), "核心观测指标", "sans", 17, st.INK_MUTED, False, "la", p, st.CARD_BG)
        st.draw_text(d, (x + 26, y + 214), focus, "sans", 23, col, True, "la", p, st.CARD_BG)


def draw_s5(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=2)
    st.draw_scene_title(d, "STEP 03 // CONSTRAINT ACCOUNTING LEDGER", "第三步：先算账，再下结论", "把待测系统拆成五本硬账，而不是拍脑袋外推趋势", t)

    lx, ly, lw, lh = 80, 224, 860, 665
    la = st.prog(t, 0.3, 0.45)
    st.draw_card(d, (lx, ly, lx + lw, ly + lh), alpha=la)
    st.draw_text(d, (lx + 34, ly + 30), "LEDGER // 预测约束台账", "mono", 16, st.COBALT, True, "la", la, st.CARD_BG)
    st.draw_text(d, (lx + 34, ly + 56), "五项必算硬约束", "serif", 28, st.INK_DARK, True, "la", la, st.CARD_BG)

    rows = [
        ("01", "存量", "现有库存、基建规模、人口年龄底座"),
        ("02", "流量", "年度新增开采、出生/退休、财政赤字"),
        ("03", "产能", "在建矿山、精炼工厂、电网接入排期"),
        ("04", "成本", "边际开采成本、替代技术价格门槛"),
        ("05", "谁买单", "政府补贴、消费者承担或企业利润承压"),
    ]
    for i, (num, k, v) in enumerate(rows):
        p = st.prog(t, 0.9 + i * 0.72, 0.5)
        ry = ly + 114 + i * 104 + (1 - p) * 14
        st.draw_card(d, (lx + 30, ry, lx + lw - 30, ry + 86), fill=st.PAPER_BG, outline=st.CARD_BORDER, radius=8, alpha=p, bg=st.CARD_BG)
        st.draw_text(d, (lx + 54, ry + 43), num, "mono", 18, st.COBALT, True, "lm", p, st.PAPER_BG)
        st.draw_text(d, (lx + 110, ry + 43), k, "serif", 26, st.INK_DARK, True, "lm", p, st.PAPER_BG)
        st.draw_text(d, (lx + 235, ry + 43), v, "sans", 22, st.INK_BODY, False, "lm", p, st.PAPER_BG)

    rx, rw = 980, 860
    b1 = st.prog(t, 4.6, 0.65)
    st.draw_card(d, (rx, 224 + (1 - b1) * 18, rx + rw, 480 + (1 - b1) * 18), fill=st.FOREST_BG, outline=st.FOREST, width=1, alpha=b1)
    st.draw_text(d, (rx + 36, 254 + (1 - b1) * 18), "BENCHMARK 01 // IEA 2024", "mono", 15, st.FOREST, True, "la", b1, st.FOREST_BG)
    st.draw_text(d, (rx + 36, 282 + (1 - b1) * 18), "国际能源署《全球关键矿产展望 2024》", "serif", 27, st.INK_DARK, True, "la", b1, st.FOREST_BG)
    st.draw_text(d, (rx + 36, 338 + (1 - b1) * 18), "66.7%", "mono", 52, st.FOREST, True, "la", b1, st.FOREST_BG)
    st.draw_text(d, (rx + 225, 352 + (1 - b1) * 18), "严格胜率（仅 3.2% 错误）", "sans", 24, st.FOREST, True, "la", b1, st.FOREST_BG)
    st.draw_text(d, (rx + 36, 418 + (1 - b1) * 18), "拆到具体金属品类、在建矿山与精炼产能份额", "sans", 21, st.INK_BODY, False, "la", b1, st.FOREST_BG)

    b2 = st.prog(t, 7.6, 0.65)
    st.draw_card(d, (rx, 512 + (1 - b2) * 18, rx + rw, 889 + (1 - b2) * 18), fill=st.ANCHOR_DARK, outline=st.ANCHOR_DARK, alpha=b2)
    st.draw_text(d, (rx + 36, 542 + (1 - b2) * 18), "BENCHMARK 02 // EDMUND BURKE 1790", "mono", 15, st.TERRACOTTA, True, "la", b2, st.ANCHOR_DARK)
    st.draw_text(d, (rx + 36, 570 + (1 - b2) * 18), "埃德蒙·伯克《法国革命论》", "serif", 28, st.INK_LIGHT, True, "la", b2, st.ANCHOR_DARK)
    st.draw_text(d, (rx + 36, 624 + (1 - b2) * 18), "31", "mono", 48, (118, 198, 152), True, "la", b2, st.ANCHOR_DARK)
    st.draw_text(d, (rx + 108, 636 + (1 - b2) * 18), "条可判定 ·", "sans", 26, st.INK_LIGHT, True, "la", b2, st.ANCHOR_DARK)
    st.draw_text(d, (rx + 260, 624 + (1 - b2) * 18), "0", "mono", 48, (118, 198, 152), True, "la", b2, st.ANCHOR_DARK)
    st.draw_text(d, (rx + 300, 636 + (1 - b2) * 18), "错误", "sans", 26, (118, 198, 152), True, "la", b2, st.ANCHOR_DARK)
    st.draw_text(d, (rx + 36, 696 + (1 - b2) * 18), "不看政治口号，只拆四本硬账：", "sans", 20, (186, 184, 178), False, "la", b2, st.ANCHOR_DARK)

    boxes = ["财政", "军队", "产权", "秩序"]
    bw2 = 176
    for i, bn in enumerate(boxes):
        bp = st.prog(t, 8.6 + i * 0.35, 0.4)
        bx = rx + 36 + i * (bw2 + 24)
        by = 750 + (1 - bp) * 12
        st.draw_card(d, (bx, by, bx + bw2, by + 95), fill=(36, 36, 33), outline=(72, 70, 64), radius=8, alpha=bp, bg=st.ANCHOR_DARK)
        st.draw_text(d, (bx + bw2 // 2, by + 48), bn, "serif", 28, st.INK_LIGHT, True, "mm", bp, (36, 36, 33))


def draw_s6(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=3)
    st.draw_scene_title(d, "STEP 04 // ACTORS & CONDITIONAL BRANCHING", "第四步：列出行动者，画出条件分支", "现实不是静态单行道，每一方都有绕行与反制能力", t)

    qs = [("01", "谁想做"), ("02", "谁有权"), ("03", "谁能绕行"), ("04", "谁买单")]
    for i, (num, q) in enumerate(qs):
        p = st.prog(t, 0.6 + i * 0.65, 0.45)
        y = 228 + i * 112 + (1 - p) * 14
        st.draw_card(d, (80, y, 600, y + 88), alpha=p)
        d.rectangle((80, y, 86, y + 88), fill=st.fade_color(st.COBALT, p))
        st.draw_text(d, (124, y + 44), num, "mono", 22, st.COBALT, True, "lm", p, st.CARD_BG)
        st.draw_text(d, (188, y + 44), q, "serif", 30, st.INK_DARK, True, "lm", p, st.CARD_BG)

    tx, ty, tw, th = 640, 228, 1200, 424
    ta = st.prog(t, 3.6, 0.5)
    st.draw_card(d, (tx, ty, tx + tw, ty + th), alpha=ta)
    st.draw_text(d, (tx + 36, ty + 32), "CONDITIONAL PROBABILITY TREE // OECD & WORLD BANK", "mono", 16, st.COBALT, True, "la", ta, st.CARD_BG)

    na = st.prog(t, 4.2, 0.45)
    ax, ay = tx + 210, ty + 230
    st.draw_card(d, (ax - 135, ay - 52, ax + 135, ay + 52), fill=st.COBALT_BG, outline=st.COBALT, alpha=na, bg=st.CARD_BG)
    st.draw_text(d, (ax, ay - 12), "前提 A 成立", "serif", 25, st.INK_DARK, True, "mm", na, st.COBALT_BG)
    st.draw_text(d, (ax, ay + 22), "P(A)", "mono", 21, st.COBALT, True, "mm", na, st.COBALT_BG)

    nb = st.prog(t, 5.0, 0.55)
    bx, by1, by2 = tx + 720, ty + 145, ty + 320
    st.draw_arrow_aa(img, (ax + 140, ay - 16), (bx - 185, by1), color=st.FOREST, width=3, alpha=nb)
    st.draw_arrow_aa(img, (ax + 140, ay + 16), (bx - 185, by2), color=st.AMBER, width=3, alpha=nb)

    st.draw_card(d, (bx - 180, by1 - 46, bx + 290, by1 + 46), fill=st.FOREST_BG, outline=st.FOREST, alpha=nb, bg=st.CARD_BG)
    st.draw_text(d, (bx + 55, by1 - 12), "走向结果 B（高情景）", "sans", 22, st.INK_DARK, True, "mm", nb, st.FOREST_BG)
    st.draw_text(d, (bx + 55, by1 + 20), "P(B | A)", "mono", 20, st.FOREST, True, "mm", nb, st.FOREST_BG)

    st.draw_card(d, (bx - 180, by2 - 46, bx + 290, by2 + 46), fill=st.AMBER_BG, outline=st.AMBER, alpha=nb, bg=st.CARD_BG)
    st.draw_text(d, (bx + 55, by2 - 12), "走向替代 / 绕行路径", "sans", 22, st.INK_DARK, True, "mm", nb, st.AMBER_BG)
    st.draw_text(d, (bx + 55, by2 + 20), "P(not B | A)", "mono", 20, st.AMBER, True, "mm", nb, st.AMBER_BG)

    ra = st.prog(t, 8.4, 0.65)
    st.draw_card(d, (80, 688 + (1 - ra) * 16, 1840, 885 + (1 - ra) * 16), fill=st.TERRACOTTA_BG, outline=st.TERRACOTTA, alpha=ra)
    st.draw_cross_mark(d, 138, 786 + (1 - ra) * 16, r=22, color=st.TERRACOTTA, alpha=ra, bg=st.TERRACOTTA_BG)
    st.draw_text(d, (186, 724 + (1 - ra) * 16), "反面例子 · 霍纳迪 (1913)《正在消失的野生生物》", "serif", 26, st.TERRACOTTA, True, "la", ra, st.TERRACOTTA_BG)
    st.draw_text(d, (186, 774 + (1 - ra) * 16), "只按当时捕猎速率外推“美洲鹤必灭绝”，忘了危机触发后人类会立法保护（国家公园与保护法案）", "sans", 23, st.INK_DARK, False, "la", ra, st.TERRACOTTA_BG)
    st.draw_text(d, (186, 822 + (1 - ra) * 16), "全书可判定 66 条，错误率高达 45.5%", "sans", 22, st.TERRACOTTA, True, "la", ra, st.TERRACOTTA_BG)


def draw_s7(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=4)
    st.draw_scene_title(d, "STEP 05 // HORIZON CALIBRATION", "第五步：按时间跨度决定你敢说多硬", "短期盯排期，中期给情景，长期只押慢变量", t)

    segs = [
        ("0 - 3 年 · 短期", "可给具体时间", "盯在建产能、施工排期、政策日程", st.FOREST, st.FOREST_BG, 0.6),
        ("5 - 15 年 · 中期", "给区间 ＋ 条件情景", "用制度激励、价值网与多情景分支", st.COBALT, st.COBALT_BG, 2.1),
        ("15 年以上 · 长期", "只押慢变量", "只押地理、人口、技术功能；不押年份与外观", st.TERRACOTTA, st.TERRACOTTA_BG, 3.6),
    ]
    sw, sh, gap = 560, 212, 40
    sx = (st.W - (3 * sw + 2 * gap)) // 2
    for i, (tl, hard, desc, col, bgc, st_t) in enumerate(segs):
        p = st.prog(t, st_t, 0.55)
        x = sx + i * (sw + gap)
        y = 228 + (1 - p) * 16
        st.draw_card(d, (x, y, x + sw, y + sh), alpha=p)
        d.rectangle((x, y, x + sw, y + 4), fill=st.fade_color(col, p))
        st.draw_text(d, (x + 28, y + 32), tl, "sans", 20, col, True, "la", p, st.CARD_BG)
        st.draw_text(d, (x + 28, y + 76), hard, "serif", 32, st.INK_DARK, True, "la", p, st.CARD_BG)
        st.draw_wrapped(d, x + 28, y + 136, desc, sw - 56, "sans", 21, st.INK_MUTED, False, 6, 2, p, st.CARD_BG)

    panels = [
        ("全库对照 (8,130 条)", "不写死日期 · 方向判断", 12.3, "写死日期 · 硬时间承诺", 17.9, 6.0, 80),
        ("UK GO-Science《制造业的未来》(2013)", "不写死日期 · 方向判断", 3.7, "写死年份 · 具体宏观预测", 56.0, 9.0, 980),
    ]
    pw, ph, py = 860, 415, 474
    for title, l1, v1, l2, v2, st_t, px in panels:
        pa = st.prog(t, st_t, 0.55)
        bp = st.prog(t, st_t + 0.25, 0.95)
        st.draw_card(d, (px, py, px + pw, py + ph), alpha=pa)
        st.draw_text(d, (px + 34, py + 32), title, "serif", 26, st.INK_DARK, True, "la", pa, st.CARD_BG)

        st.draw_text(d, (px + 34, py + 112), l1, "sans", 22, st.FOREST, True, "la", pa, st.CARD_BG)
        w1 = max(8, int((v1 / 65.0) * 600 * bp))
        d.rectangle((px + 34, py + 154, px + 34 + w1, py + 196), fill=st.fade_color(st.FOREST, pa, st.CARD_BG))
        st.draw_text(d, (px + 48 + w1, py + 175), f"错误率 {v1 * bp:.1f}%", "sans", 23, st.FOREST, True, "lm", pa, st.CARD_BG)

        st.draw_text(d, (px + 34, py + 248), l2, "sans", 22, st.TERRACOTTA, True, "la", pa, st.CARD_BG)
        w2 = max(8, int((v2 / 65.0) * 600 * bp))
        d.rectangle((px + 34, py + 290, px + 34 + w2, py + 332), fill=st.fade_color(st.TERRACOTTA, pa, st.CARD_BG))
        st.draw_text(d, (px + 48 + w2, py + 311), f"错误率 {v2 * bp:.1f}%", "sans", 23, st.TERRACOTTA, True, "lm", pa, st.CARD_BG)


def draw_s8(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=5)
    st.draw_scene_title(d, "STEP 06 // FAILURE PATTERN CHECKLIST", "第六步：五大翻车模式扫雷", "复盘全库 689 条“错误”总结出的高频失手死因", t)

    items = [
        ("01", "忽略替代与技术跃迁", "马尔萨斯(1798)：忽视农业育种与化肥，错误率 59.1%", 0.7),
        ("02", "把方向偷换成固定速率 / 极端量词", "安德森：“几乎每首歌都会卖掉”“边际成本每年降 50%”", 2.7),
        ("03", "跨层跳跃（技术可行 → 社会终局）", "戴维(1919)：从航空普及直接跳到“消灭战争与民族主义”", 5.0),
        ("04", "忽略行动者的绕行与政策反制", "霍纳迪漏算保护立法；马凯硕漏算转道越南/墨西哥绕行", 7.6),
        ("05", "把阶段顺风当成永久直线", "费雪(1920)外推通胀；库兹韦尔(2024)外推疫情远程办公", 10.0),
    ]
    for i, (num, head, case, st_t) in enumerate(items):
        p = st.prog(t, st_t, 0.5)
        y = 222 + i * 105 + (1 - p) * 14
        st.draw_card(d, (80, y, 1840, y + 90), alpha=p)
        st.draw_cross_mark(d, 132, y + 45, r=18, color=st.TERRACOTTA, alpha=p, bg=st.CARD_BG)
        st.draw_text(d, (176, y + 20), num, "mono", 18, st.TERRACOTTA, True, "la", p, st.CARD_BG)
        st.draw_text(d, (218, y + 16), head, "serif", 26, st.INK_DARK, True, "la", p, st.CARD_BG)
        st.draw_text(d, (176, y + 54), case, "sans", 20, st.INK_MUTED, False, "la", p, st.CARD_BG)

    sa = st.prog(t, 12.2, 0.55)
    st.draw_card(d, (80, 766 + (1 - sa) * 14, 1840, 886 + (1 - sa) * 14), fill=st.ANCHOR_DARK, outline=st.ANCHOR_DARK, alpha=sa)
    st.draw_text(d, (130, 826 + (1 - sa) * 14), "红灯句式：“无论如何都必将……”   “永远不会……”   “到某年几乎全部……”", "sans", 26, st.INK_LIGHT, True, "lm", sa, st.ANCHOR_DARK)
    sp = st.prog(t, 13.0, 0.35)
    if sp > 0.05:
        d.rounded_rectangle((1560, 790, 1795, 862), radius=8, fill=st.fade_color(st.TERRACOTTA, sp, st.ANCHOR_DARK))
        st.draw_text(d, (1677, 826), "直接降权", "serif", 30, st.INK_LIGHT, True, "mm", sp, st.TERRACOTTA)


def draw_s9(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, active=6)
    st.draw_scene_title(d, "STEP 07 // PRE-FREEZE & 3-AXIS REVIEW", "第七步：事前冻结，事后三轴复盘", "把灵感猜想升级成可追溯、可纠偏的科学记录系统", t)

    ca = st.prog(t, 0.35, 0.55)
    cx, cy, cw, ch = 80, 228, 790, 650
    st.draw_card(d, (cx, cy, cx + cw, cy + ch), alpha=ca)
    st.draw_text(d, (cx + 34, cy + 32), "FORECAST CARD // FROZEN RECORD", "mono", 15, st.COBALT, True, "la", ca, st.CARD_BG)
    st.draw_text(d, (cx + 34, cy + 56), "标准预测卡（事前冻结）", "serif", 28, st.INK_DARK, True, "la", ca, st.CARD_BG)

    fields = [
        ("命题", "具体主体 ＋ 对象 ＋ 量词 ＋ 指标"),
        ("期限", "明确到窗口区间或具体年份"),
        ("条件", "前提 A 及其触发边界"),
        ("依据", "账本数据与机制透镜"),
        ("复盘日", "到期前设定固定核验日期"),
    ]
    for i, (fk, fv) in enumerate(fields):
        fp = st.prog(t, 0.8 + i * 0.45, 0.42)
        fy = cy + 114 + i * 102
        st.draw_card(d, (cx + 32, fy, cx + cw - 32, fy + 82), fill=st.PAPER_BG, outline=st.CARD_BORDER, radius=8, alpha=fp, bg=st.CARD_BG)
        st.draw_text(d, (cx + 56, fy + 41), fk, "serif", 24, st.COBALT, True, "lm", fp, st.PAPER_BG)
        st.draw_text(d, (cx + 185, fy + 41), fv, "sans", 22, st.INK_BODY, False, "lm", fp, st.PAPER_BG)

    la = st.prog(t, 3.4, 0.45)
    if la > 0.05:
        st.draw_pill(d, cx + cw - 32, cy + 44, "已冻结 2026-11-24", st.FOREST, st.FOREST_BG, 18, la, st.CARD_BG)

    axes = [
        ("AXIS 01", "事件轴 · 发生了吗？", "只核对客观事实有没有兑现，不替自己找借口", st.FOREST, 5.0),
        ("AXIS 02", "机制轴 · 理由对吗？", "结果猜对 != 归因成立；别把运气当本事", st.COBALT, 7.0),
        ("AXIS 03", "时间轴 · 准时吗？", "方向对了但晚了十年，时间分一样要扣", st.TERRACOTTA, 9.0),
    ]
    rx, rw = 910, 930
    for i, (ak, at, ad, col, st_t) in enumerate(axes):
        p = st.prog(t, st_t, 0.55)
        ay = 228 + i * 224 + (1 - p) * 16
        st.draw_card(d, (rx, ay, rx + rw, ay + 196), alpha=p)
        d.rectangle((rx, ay, rx + 5, ay + 196), fill=st.fade_color(col, p))
        st.draw_text(d, (rx + 36, ay + 34), ak, "mono", 16, col, True, "la", p, st.CARD_BG)
        st.draw_text(d, (rx + 36, ay + 66), at, "serif", 32, st.INK_DARK, True, "la", p, st.CARD_BG)
        st.draw_text(d, (rx + 36, ay + 128), ad, "sans", 23, st.INK_BODY, False, "la", p, st.CARD_BG)


def draw_s10(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, all_done=True)
    st.draw_scene_title(d, "WORKFLOW DEMO // US DATA CENTER POWER (2025 - 2030)", "实战演示：未来 5 年美国数据中心用电", "把 7 个步骤串成一条完整可核验的工作流", t)
    st.draw_pill(d, 1840, 108, "示范流程，不代表结论", st.AMBER, st.AMBER_BG, 20, 1.0, st.PAPER_BG)

    rows = [
        ("01", "拆题", "到 2030 年，美国数据中心用电占比比 2025 年至少提高 2 个百分点", st.COBALT, 2.0),
        ("02", "选老师", "主透镜：IEA 电力账本  ｜  反校验：杰文斯悖论（能效提升推高需求）", st.FOREST, 5.8),
        ("03", "先算账", "列出在建数据中心装机、电网接入排队、芯片单位算力功耗", st.COBALT, 9.0),
        ("04", "画分支", "若电网审批提速 -> 走高情景；若审批/地方限批受阻 -> 走低情景", st.AMBER, 12.2),
        ("05", "定硬度", "5 年属中期：给占比区间与情景，不赌单一精确年份", st.COBALT, 15.8),
        ("06", "扫雷", "检查是否漏算芯片能效跃迁与地方电网限批反制", st.TERRACOTTA, 18.8),
        ("07", "冻结复盘", "锁定卡片，每年对照 EIA 用电与电网审批数据复盘一次", st.FOREST, 21.6),
    ]
    for i, (num, sk, sv, col, st_t) in enumerate(rows):
        p = st.prog(t, st_t, 0.5)
        y = 222 + i * 95 + (1 - p) * 12
        st.draw_card(d, (80, y, 1840, y + 82), alpha=p)
        d.rectangle((80, y, 86, y + 82), fill=st.fade_color(col, p))
        st.draw_text(d, (118, y + 41), num, "mono", 19, col, True, "lm", p, st.CARD_BG)
        st.draw_text(d, (168, y + 41), sk, "serif", 24, st.INK_DARK, True, "lm", p, st.CARD_BG)
        st.draw_text(d, (315, y + 41), sv, "sans", 23, st.INK_BODY, False, "lm", p, st.CARD_BG)


def draw_s11(img: Image.Image, d: ImageDraw.ImageDraw, t: float, dur: float):
    hdr(d, all_done=True)
    st.draw_text(d, (st.W // 2, 165), "SYNTHESIS // THREE PRINCIPLES", "mono", 18, st.TERRACOTTA, False, "mm", st.prog(t, 0.1, 0.45))

    lines = [
        ("01", "方向，用结构来押", st.COBALT, 0.4, False),
        ("02", "时间，用账本来押", st.FOREST, 1.9, False),
        ("03", "绝对化的话，直接降权", st.TERRACOTTA, 3.4, True),
    ]
    for i, (num, txt, col, st_t, dark) in enumerate(lines):
        p = st.prog(t, st_t, 0.6)
        y = 285 + i * 136 + (1 - p) * 18
        bg_c = st.ANCHOR_DARK if dark else st.CARD_BG
        st.draw_card(d, (340, y - 48, 1580, y + 48), fill=bg_c, outline=col if dark else st.CARD_BORDER, alpha=p)
        d.rectangle((340, y - 48, 346, y + 48), fill=st.fade_color(col, p))
        st.draw_text(d, (405, y), num, "mono", 24, col, True, "lm", p, bg_c)
        st.draw_text(d, (st.W // 2 + 20, y), txt, "serif", 42, st.INK_LIGHT if dark else st.INK_DARK, True, "mm", p, bg_c)

    qa = st.prog(t, 5.2, 0.65)
    st.draw_text(d, (st.W // 2, 740 + (1 - qa) * 12), "“最好的预测者不是更会猜，而是更清楚自己会在哪一步错。”", "serif", 30, st.INK_DARK, True, "mm", qa)
    fa = st.prog(t, 6.2, 0.5)
    st.draw_text(d, (st.W // 2, 822), "SOURCE // FORECAST-LAB · 132 WORKS · 8,130 FORECASTS · 5,060 DECIDED", "mono", 17, st.INK_MUTED, False, "mm", fa)


SCENES = [
    {"id": "s0", "name": "S0 片头", "voice": st.VOICE_MALE, "draw": draw_s0,
     "narration": "我们复盘了一百三十二本预测类著作，总共八千一百三十条预测，其中五千零六十条现在已经能判出对错。这个视频，用七个步骤手把手教你：怎样像其中最准的那批人一样做预测，又怎样避开他们最常踩的坑。"},
    {"id": "s1", "name": "S1 成绩单：没有全能先知", "voice": st.VOICE_MALE, "draw": draw_s1,
     "narration": "先看成绩单。全库没有全能先知。最准的不是预言家，而是带着约束账本的专业机构：国际机构与政府智库，严格胜率百分之四十七，错误率只有百分之六点三。科幻和乌托邦作家严格胜率不到三成，错误率超过三成。同一个作者换个领域，成绩也会塌：威尔斯一九零一年的《预言》严格胜率百分之五十二，到了构想世界政府的《公开的阴谋》，错误率飙到百分之四十一。"},
    {"id": "s2", "name": "S2 底线：时间越远越难", "voice": st.VOICE_FEMALE, "draw": draw_s2,
     "narration": "第二个底线：时间越远越难。出版不到三年的书，错误率只有百分之二点九；跨越二三十年，升到百分之十左右；跨越四十年以上，错误率达到百分之二十五到四十。库兹韦尔二零二四年的新书，九成预测还没到期；而他二零零五年的书，经过二十年检验，只有百分之五点四完全说对。所以评价任何人，只和同样时间跨度的人比。"},
    {"id": "s3", "name": "S3 第一步 拆题", "voice": st.VOICE_MALE, "draw": draw_s3,
     "narration": "第一步，把大判断拆成可检验的命题。一条合格的预测，要写清楚六样东西：主体、对象、量词、指标、期限、条件。比如“AI会取代大量工作”，就要改写成：在没有大规模监管的前提下，到二零三零年，美国白领岗位数比二零二五年下降至少百分之十。还要警惕偷换：出现，不等于普及；普及，不等于主导；主导，不等于取代。"},
    {"id": "s4", "name": "S4 第二步 按领域选老师", "voice": st.VOICE_FEMALE, "draw": draw_s4,
     "narration": "第二步，按领域选对老师。地缘政治，学扎卡利亚、卡普兰和李光耀，看地理底盘和大国利益约束。宏观金融，学达利欧的债务机制和塔勒布的风险不对称，别学点位预测。产业颠覆，学克里斯坦森，看在位者的利润包袱。人工智能，学博斯特罗姆的条件判断，再配上能源署的电力账本。能源资源，学国际能源署和杰文斯，按矿种、产能逐项算账。社会制度，学伯克，看财政、军纪、产权和社会黏合剂。"},
    {"id": "s5", "name": "S5 第三步 先算账", "voice": st.VOICE_MALE, "draw": draw_s5,
     "narration": "第三步，先算账，再下结论。把系统拆成存量、流量、产能、成本，以及谁来买单。国际能源署的关键矿产展望就是这样做的：拆到具体金属、在建矿山和精炼产能，严格胜率达到百分之六十七。伯克在一七九零年用财政、军队、产权和社会秩序四本账判断法国革命的走向，三十一条可判定预测，零错误。"},
    {"id": "s6", "name": "S6 第四步 行动者与条件分支", "voice": st.VOICE_FEMALE, "draw": draw_s6,
     "narration": "第四步，列出行动者，画出条件分支。问四个问题：谁想做，谁有权，谁能绕行，谁来买单。然后把前提A发生的概率，和A发生后B发生的概率分开记账。经合组织和世界银行的报告，几乎都用情景分支写作，错误率极低。反面例子是霍纳迪：他按一九一三年的捕猎速度，断言美洲鹤必然灭绝，却忘了社会会立法保护，错误率百分之四十五。"},
    {"id": "s7", "name": "S7 第五步 按时间跨度定硬度", "voice": st.VOICE_MALE, "draw": draw_s7,
     "narration": "第五步，按时间跨度决定你敢说多硬。三年以内，盯在建产能和政策日程，可以给出具体时间。五到十五年，用制度激励和多情景分支。十五年以上，只押地理、人口和技术功能这类慢变量，不押具体年份和具体外观。数据显示，写死日期的预测，错误率百分之十八，不写死日期的方向判断，错误率百分之十二。英国政府科学办公室二零一三年的制造业报告，方向判断错误率不到百分之四，写死年份的判断，错误率高达百分之五十六。"},
    {"id": "s8", "name": "S8 第六步 五大翻车模式扫雷", "voice": st.VOICE_FEMALE, "draw": draw_s8,
     "narration": "第六步，用五个反面清单给自己扫雷。一，忽略替代和技术跃迁，马尔萨斯的错误率百分之五十九。二，把方向对偷换成固定速率或者“几乎全部”这种极端量词。三，跨层跳跃，从技术可行直接跳到社会终局，比如“飞机会消灭战争”。四，忽略行动者的绕行和政策反制。五，把一段顺风当成永久直线。只要看到“无论如何都必将”“永远不会”，就直接降权。"},
    {"id": "s9", "name": "S9 第七步 冻结与三轴复盘", "voice": st.VOICE_MALE, "draw": draw_s9,
     "narration": "第七步，事前冻结，事后三轴复盘。把预测写成卡片，标上日期和更新时间点，不许事后改。到期时分三条轴复盘：事件发生了没有，机制对不对，时间准不准。结果猜对，不代表你的理由对；方向对了但晚了十年，时间分一样要扣。"},
    {"id": "s10", "name": "S10 实战演示", "voice": st.VOICE_FEMALE, "draw": draw_s10,
     "narration": "最后做一次完整演示。问题是：未来五年，美国数据中心用电会怎样？第一步，命题写成：到二零三零年，美国数据中心用电占全国比例，较二零二五年至少提高两个百分点。第二步，主透镜用能源署的电力账本，反校验用杰文斯悖论。第三步，账本里列出在建数据中心、电网接入排队和芯片能效。第四步，分支：如果电网审批提速，走高情景；如果审批受阻，走低情景。第五步，五年属于中期，给区间，不给精确年份。第六步，扫雷：有没有忽略能效提升和地方限批？第七步，冻结卡片，每年复盘一次。"},
    {"id": "s11", "name": "S11 结尾", "voice": st.VOICE_MALE, "draw": draw_s11,
     "narration": "记住三句话：方向，用结构来押；时间，用账本来押；绝对化的话，直接降权。最好的预测者不是更会猜，而是更清楚自己会在哪一步错。"},
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", help="只重渲染指定场景 id (如 s2)")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SCRATCH_DIR.mkdir(parents=True, exist_ok=True)

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
        wav_path, adur, dur, subs = st.prepare_neural_audio(sc, SCRATCH_DIR, rate="+4%")
        st.render_scene_pipeline(sc, wav_path, dur, subs, sc["draw"], SCRATCH_DIR)
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
