#!/usr/bin/env python3
"""
Anthropic x Kimi 科研档案视觉与神经网络双人配音共用引擎
"""
import json
import math
import re
import shutil
import subprocess
import time
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.io import wavfile

W, H = 1920, 1080
FPS = 30

FONT_SERIF = "/System/Library/Fonts/Supplemental/Songti.ttc"
FONT_SANS = "/System/Library/Fonts/Hiragino Sans GB.ttc"
FONT_MONO = "/System/Library/Fonts/SFNSMono.ttf"
UVX_BIN = shutil.which("uvx") or "uvx"

# Anthropic x Kimi 科研档案色彩系统
PAPER_BG = (246, 244, 238)       # #F6F4EE
GRID_LINE = (234, 230, 220)      # #EAE6DC
REG_MARK = (196, 190, 178)       # #C4BEB2
CARD_BG = (252, 251, 248)        # #FCFBF8
CARD_BORDER = (220, 215, 204)    # #DCD7CC
ANCHOR_DARK = (24, 24, 22)       # #181816

INK_DARK = (20, 20, 19)          # #141413
INK_BODY = (56, 55, 51)          # #383733
INK_MUTED = (120, 116, 108)      # #78746C
INK_LIGHT = (246, 244, 238)      # #F6F4EE

TERRACOTTA = (200, 90, 58)       # #C85A3A
TERRACOTTA_BG = (247, 235, 230)  # #F7EBE6
COBALT = (43, 91, 132)           # #2B5B84
COBALT_BG = (235, 241, 246)      # #EBF1F6
FOREST = (61, 107, 82)           # #3D6B52
FOREST_BG = (234, 241, 236)      # #EAF1EC
AMBER = (166, 110, 40)           # #A66E28
AMBER_BG = (246, 239, 228)       # #F6EFE4

VOICE_MALE = "zh-CN-YunyangNeural"
VOICE_FEMALE = "zh-CN-XiaoxiaoNeural"

_FONT_CACHE = {}


def get_font(family: str, size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    key = (family, size, bold)
    if key not in _FONT_CACHE:
        if family == "serif":
            _FONT_CACHE[key] = ImageFont.truetype(FONT_SERIF, size, index=(1 if bold else 6))
        elif family == "mono":
            _FONT_CACHE[key] = ImageFont.truetype(FONT_MONO, size, index=0)
        else:
            _FONT_CACHE[key] = ImageFont.truetype(FONT_SANS, size, index=(2 if bold else 0))
    return _FONT_CACHE[key]


def build_paper_bg() -> Image.Image:
    rng = np.random.default_rng(42)
    base = np.zeros((H, W, 3), dtype=np.int16)
    base[:, :, 0] = PAPER_BG[0]
    base[:, :, 1] = PAPER_BG[1]
    base[:, :, 2] = PAPER_BG[2]
    noise = rng.integers(-2, 3, size=(H, W, 1), dtype=np.int16)
    arr = np.clip(base + noise, 0, 255).astype(np.uint8)
    img = Image.fromarray(arr, mode="RGB")
    d = ImageDraw.Draw(img)
    # 极淡坐标网格
    for x in range(80, W, 160):
        d.line([(x, 76), (x, H - 40)], fill=GRID_LINE, width=1)
    for y in range(140, H - 40, 160):
        d.line([(40, y), (W - 40, y)], fill=GRID_LINE, width=1)
    # 四角精密十字对位标
    for cx, cy in [(36, 36), (W - 36, 36), (36, H - 36), (W - 36, H - 36)]:
        d.line([(cx - 10, cy), (cx + 10, cy)], fill=REG_MARK, width=1)
        d.line([(cx, cy - 10), (cx, cy + 10)], fill=REG_MARK, width=1)
    return img


BG_IMG = build_paper_bg()


def clamp(v: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return lo if v < lo else (hi if v > hi else v)


def ease_out_quint(x: float) -> float:
    x = clamp(x)
    return 1.0 - (1.0 - x) ** 5


def prog(t: float, start: float, duration: float = 0.55) -> float:
    return ease_out_quint((t - start) / duration)


def blend(c1, c2, alpha: float):
    a = clamp(alpha)
    return (
        int(c1[0] + (c2[0] - c1[0]) * a),
        int(c1[1] + (c2[1] - c1[1]) * a),
        int(c1[2] + (c2[2] - c1[2]) * a),
    )


def fade_color(color, alpha: float, bg=PAPER_BG):
    return blend(bg, color, alpha)


def draw_text(
    draw: ImageDraw.ImageDraw,
    xy,
    text: str,
    family: str = "sans",
    size: int = 24,
    color=INK_DARK,
    bold: bool = False,
    anchor: str = "la",
    alpha: float = 1.0,
    bg=PAPER_BG,
):
    if alpha <= 0.01:
        return
    c = fade_color(color, alpha, bg) if alpha < 0.999 else color
    draw.text(xy, text, font=get_font(family, size, bold), fill=c, anchor=anchor)


def text_width(text: str, family: str = "sans", size: int = 24, bold: bool = False) -> float:
    return get_font(family, size, bold).getlength(text)


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    x: float,
    y: float,
    text: str,
    max_w: float,
    family: str = "sans",
    size: int = 22,
    color=INK_BODY,
    bold: bool = False,
    line_gap: int = 8,
    max_lines: int = 4,
    alpha: float = 1.0,
    bg=CARD_BG,
) -> float:
    if alpha <= 0.01:
        return y
    f = get_font(family, size, bold)
    lines, cur = [], ""
    for ch in text:
        if ch == "\n":
            lines.append(cur)
            cur = ""
            if len(lines) >= max_lines:
                break
            continue
        if f.getlength(cur + ch) <= max_w:
            cur += ch
        else:
            lines.append(cur)
            cur = ch
            if len(lines) >= max_lines:
                break
    if cur and len(lines) < max_lines:
        lines.append(cur)
    if len(lines) == max_lines and len("".join(lines)) < len(text.replace("\n", "")):
        lines[-1] = lines[-1][:-1] + "…"
    c = fade_color(color, alpha, bg) if alpha < 0.999 else color
    cy = y
    for ln in lines:
        draw.text((x, cy), ln, font=f, fill=c, anchor="la")
        cy += size + line_gap
    return cy


def draw_card(
    draw: ImageDraw.ImageDraw,
    box,
    fill=CARD_BG,
    outline=CARD_BORDER,
    radius: int = 10,
    width: int = 1,
    alpha: float = 1.0,
    bg=PAPER_BG,
):
    if alpha <= 0.01:
        return
    f = fade_color(fill, alpha, bg) if alpha < 0.999 else fill
    o = fade_color(outline, alpha, bg) if (outline and alpha < 0.999) else outline
    draw.rounded_rectangle(box, radius=radius, fill=f, outline=o, width=width if o else 0)


def draw_pill(
    draw: ImageDraw.ImageDraw,
    x_right: float,
    y_top: float,
    text: str,
    text_color=COBALT,
    bg_color=COBALT_BG,
    size: int = 17,
    alpha: float = 1.0,
    parent_bg=CARD_BG,
):
    if alpha <= 0.01:
        return
    tw = int(text_width(text, "sans", size, True)) + 20
    x0 = x_right - tw
    draw.rounded_rectangle(
        (x0, y_top, x_right, y_top + size + 10),
        radius=6,
        fill=fade_color(bg_color, alpha, parent_bg),
    )
    draw_text(draw, (x0 + tw / 2, y_top + (size + 10) / 2), text, "sans", size, text_color, True, "mm", alpha, bg_color)


def draw_dashed_line(draw: ImageDraw.ImageDraw, p1, p2, fill=REG_MARK, width: int = 1, dash: int = 8, gap: int = 6):
    x1, y1 = p1
    x2, y2 = p2
    dist = math.hypot(x2 - x1, y2 - y1)
    if dist < 1:
        return
    dx, dy = (x2 - x1) / dist, (y2 - y1) / dist
    cur = 0.0
    while cur < dist:
        nxt = min(dist, cur + dash)
        draw.line([(x1 + dx * cur, y1 + dy * cur), (x1 + dx * nxt, y1 + dy * nxt)], fill=fill, width=width)
        cur = nxt + gap


def draw_arrow_aa(img: Image.Image, p1, p2, color=COBALT, width: int = 3, head: int = 12, alpha: float = 1.0):
    if alpha <= 0.01:
        return
    pad = 24
    x0 = int(min(p1[0], p2[0]) - pad)
    y0 = int(min(p1[1], p2[1]) - pad)
    x1 = int(max(p1[0], p2[0]) + pad)
    y1 = int(max(p1[1], p2[1]) + pad)
    pw, ph = max(1, x1 - x0), max(1, y1 - y0)
    patch = Image.new("RGBA", (pw * 2, ph * 2), (0, 0, 0, 0))
    pd = ImageDraw.Draw(patch)
    q1 = ((p1[0] - x0) * 2, (p1[1] - y0) * 2)
    q2 = ((p2[0] - x0) * 2, (p2[1] - y0) * 2)
    col = (*color, int(255 * clamp(alpha)))
    pd.line([q1, q2], fill=col, width=width * 2)
    ang = math.atan2(q2[1] - q1[1], q2[0] - q1[0])
    a1, a2 = ang + math.pi * 0.82, ang - math.pi * 0.82
    h2 = head * 2
    pd.polygon(
        [q2, (q2[0] + h2 * math.cos(a1), q2[1] + h2 * math.sin(a1)), (q2[0] + h2 * math.cos(a2), q2[1] + h2 * math.sin(a2))],
        fill=col,
    )
    patch = patch.resize((pw, ph), Image.Resampling.LANCZOS)
    img.paste(patch, (x0, y0), patch)


def draw_polyline_aa(img: Image.Image, pts, color=COBALT, width: int = 4, alpha: float = 1.0):
    if len(pts) < 2 or alpha <= 0.01:
        return
    pad = 16
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    x0, y0 = int(min(xs) - pad), int(min(ys) - pad)
    x1, y1 = int(max(xs) + pad), int(max(ys) + pad)
    pw, ph = max(1, x1 - x0), max(1, y1 - y0)
    patch = Image.new("RGBA", (pw * 2, ph * 2), (0, 0, 0, 0))
    pd = ImageDraw.Draw(patch)
    qpts = [((p[0] - x0) * 2, (p[1] - y0) * 2) for p in pts]
    col = (*color, int(255 * clamp(alpha)))
    pd.line(qpts, fill=col, width=width * 2, joint="curve")
    patch = patch.resize((pw, ph), Image.Resampling.LANCZOS)
    img.paste(patch, (x0, y0), patch)


def draw_cross_mark(draw: ImageDraw.ImageDraw, cx: float, cy: float, r: float = 14, color=TERRACOTTA, alpha: float = 1.0, bg=CARD_BG):
    if alpha <= 0.01:
        return
    c = fade_color(color, alpha, bg)
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=c, width=2)
    d = r * 0.42
    draw.line([(cx - d, cy - d), (cx + d, cy + d)], fill=c, width=3)
    draw.line([(cx - d, cy + d), (cx + d, cy - d)], fill=c, width=3)


def draw_header(
    draw: ImageDraw.ImageDraw,
    archive_tag: str,
    nodes: list[str],
    active_idx: int = -1,
    all_done: bool = False,
):
    """极简科研眉栏 + 刻度步骤尺"""
    draw.rectangle((0, 0, W, 68), fill=PAPER_BG)
    draw.line([(72, 68), (W - 72, 68)], fill=CARD_BORDER, width=1)
    draw_text(draw, (80, 34), archive_tag, "mono", 17, INK_MUTED, False, "lm")

    # 右侧步骤尺
    rx_end = W - 80
    step_gap = 128
    rx_start = rx_end - (len(nodes) - 1) * step_gap
    cy = 34
    for i, lbl in enumerate(nodes):
        cx = rx_start + i * step_gap
        is_cur = (i == active_idx) and not all_done
        is_done = all_done or (active_idx >= 0 and i < active_idx)
        if is_cur:
            draw.ellipse((cx - 48, cy - 4, cx - 40, cy + 4), fill=TERRACOTTA)
            draw_text(draw, (cx - 32, cy), lbl, "sans", 18, INK_DARK, True, "lm")
            draw.line([(cx - 48, 67), (cx + 46, 67)], fill=TERRACOTTA, width=3)
        elif is_done:
            draw.ellipse((cx - 46, cy - 3, cx - 40, cy + 3), fill=FOREST)
            draw_text(draw, (cx - 32, cy), lbl, "sans", 17, FOREST, True, "lm")
        else:
            draw.ellipse((cx - 46, cy - 3, cx - 40, cy + 3), outline=REG_MARK, width=1)
            draw_text(draw, (cx - 32, cy), lbl, "sans", 17, INK_MUTED, False, "lm")


def draw_scene_title(draw: ImageDraw.ImageDraw, fig_label: str, title: str, subtitle: str, t: float):
    a = prog(t, 0.0, 0.5)
    dy = (1 - a) * 14
    draw_text(draw, (80, 82 + dy), fig_label, "mono", 16, TERRACOTTA, False, "la", a)
    draw_text(draw, (80, 104 + dy), title, "serif", 44, INK_DARK, True, "la", a)
    a2 = prog(t, 0.12, 0.5)
    draw_text(draw, (80, 164 + (1 - a2) * 10), subtitle, "sans", 21, INK_MUTED, False, "la", a2)
    # 延展细线
    lp = prog(t, 0.05, 0.65)
    draw.line([(80, 200), (80 + int((W - 160) * lp), 200)], fill=CARD_BORDER, width=1)


# ------------------------------------------------------------------------------
# 字幕渲染（深炭黑档案条，在纸白底上高对比可读）
# ------------------------------------------------------------------------------

def wrap_subtitle(text: str, size: int = 29, max_w: int = 1520):
    f = get_font("sans", size, bold=True)
    text = text.strip()
    if f.getlength(text) <= max_w:
        return [text]
    mid = len(text) // 2
    best_idx, best_dist = None, 10**9
    for idx, ch in enumerate(text):
        if ch in "，、：；" and 4 < idx < len(text) - 4:
            if f.getlength(text[: idx + 1]) <= max_w and f.getlength(text[idx + 1 :]) <= max_w:
                if abs(idx - mid) < best_dist:
                    best_dist = abs(idx - mid)
                    best_idx = idx + 1
    if best_idx is not None:
        return [text[:best_idx], text[best_idx:]]
    lines, cur = [], ""
    for ch in text:
        if f.getlength(cur + ch) <= max_w:
            cur += ch
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines[:2]


def draw_subtitle(img: Image.Image, text: str):
    if not text:
        return
    size = 29
    lines = wrap_subtitle(text, size=size)
    f = get_font("sans", size, bold=True)
    max_lw = max(f.getlength(ln) for ln in lines)
    pad_x, pad_y = 28, 12
    lh = size + 8
    box_w = int(max_lw + pad_x * 2)
    box_h = int(len(lines) * lh + pad_y * 2 - 4)
    x0 = (W - box_w) // 2
    y1 = H - 24
    y0 = y1 - box_h
    overlay = Image.new("RGBA", (box_w, box_h), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rounded_rectangle((0, 0, box_w, box_h), radius=10, fill=(24, 24, 22, 232))
    img.paste(overlay, (x0, y0), overlay)
    d = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        d.text((W // 2, y0 + pad_y + i * lh), ln, font=f, fill=INK_LIGHT, anchor="ma")


# ------------------------------------------------------------------------------
# edge-tts 神经网络配音 + 科研环境声底混音管线
# ------------------------------------------------------------------------------

def _parse_srt_ts(ts: str) -> float:
    h, m, s_ms = ts.strip().split(":")
    s, ms = s_ms.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def parse_edge_srt(srt_path: Path, offset_sec: float = 0.4):
    raw = srt_path.read_text(encoding="utf-8").strip()
    if not raw:
        return []
    blocks = re.split(r"\r?\n\r?\n", raw)
    out = []
    for blk in blocks:
        lines = [ln.strip() for ln in blk.splitlines() if ln.strip()]
        if len(lines) >= 3 and "-->" in lines[1]:
            t0_s, t1_s = lines[1].split("-->")
            txt = " ".join(lines[2:])
            out.append((_parse_srt_ts(t0_s) + offset_sec, _parse_srt_ts(t1_s) + offset_sec, txt))
    return out


def split_subtitles_fallback(narration: str, start_t: float, audio_dur: float):
    parts = [s.strip() for s in re.split(r"(?<=[。！？；])", narration) if s.strip()]
    total_chars = sum(max(1, len(p)) for p in parts)
    segs, cur = [], start_t
    for p in parts:
        dt = audio_dur * (max(1, len(p)) / total_chars)
        segs.append((cur, cur + dt, p))
        cur += dt
    if segs:
        segs[-1] = (segs[-1][0], start_t + audio_dur + 0.25, segs[-1][2])
    return segs


def ffprobe_duration(path: Path) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        text=True,
    ).strip()
    return float(out)


def _synthesize_ambient_bed(n_samples: int, sr: int = 44100) -> np.ndarray:
    """纯净温暖的科研环境泛音底垫 + 开场 0.15s 极轻柔声学泛音点缀"""
    t = np.arange(n_samples, dtype=np.float64) / sr
    # D2 / A2 / E3 / F#3 温暖五度-九度和声极低音垫 (~ -29 dB)
    pad = (
        0.42 * np.sin(2 * np.pi * 73.42 * t)
        + 0.30 * np.sin(2 * np.pi * 110.00 * t)
        + 0.18 * np.sin(2 * np.pi * 164.81 * t)
        + 0.10 * np.sin(2 * np.pi * 220.00 * t)
    )
    # 缓慢呼吸包络 (0.18 Hz) + 头尾 0.35s 淡入淡出
    breath = 0.72 + 0.28 * np.sin(2 * np.pi * 0.14 * t - np.pi / 2)
    fade_len = min(int(0.35 * sr), n_samples // 4)
    env = np.ones(n_samples, dtype=np.float64)
    if fade_len > 0:
        env[:fade_len] = np.linspace(0.0, 1.0, fade_len)
        env[-fade_len:] = np.linspace(1.0, 0.0, fade_len)
    bed = pad * breath * env * 0.032

    # 开场 0.15s 轻柔声学泛音点缀 (180ms 衰减, -25 dB)
    c_start = int(0.15 * sr)
    c_len = int(0.26 * sr)
    if c_start + c_len < n_samples:
        ct = np.arange(c_len, dtype=np.float64) / sr
        chime = (0.65 * np.sin(2 * np.pi * 659.25 * ct) + 0.35 * np.sin(2 * np.pi * 987.77 * ct)) * np.exp(-ct * 16.0) * np.minimum(1.0, ct / 0.008)
        bed[c_start : c_start + c_len] += chime * 0.055

    stereo = np.stack([bed, bed], axis=1)
    return stereo


def prepare_neural_audio(scene: dict, scratch_dir: Path, rate: str = "+4%") -> tuple[Path, float, float, list]:
    sid = scene["id"]
    voice = scene.get("voice", VOICE_MALE)
    mp3_path = scratch_dir / f"{sid}_tts.mp3"
    raw_srt = scratch_dir / f"{sid}_tts.srt"
    pad_wav = scratch_dir / f"{sid}_pad.wav"
    mix_wav = scratch_dir / f"{sid}_mix.wav"

    last_err = None
    for attempt in range(3):
        try:
            subprocess.run(
                [
                    UVX_BIN, "edge-tts",
                    "--voice", voice,
                    "--rate", rate,
                    "--text", scene["narration"],
                    "--write-media", str(mp3_path),
                    "--write-subtitles", str(raw_srt),
                    "--no-progress",
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
            )
            last_err = None
            break
        except subprocess.CalledProcessError as e:
            last_err = e
            time.sleep(1.5)
    if last_err is not None:
        raise RuntimeError(f"edge-tts failed for {sid}: {last_err.stderr}")

    adur = ffprobe_duration(mp3_path)
    dur = round(adur + 1.0, 3)

    # 先转为 44100Hz stereo WAV (0.4s 延迟 + 结尾留白)
    subprocess.run(
        [
            "ffmpeg", "-y", "-v", "error", "-i", str(mp3_path),
            "-af", "adelay=400|400,apad", "-t", f"{dur:.3f}",
            "-ar", "44100", "-ac", "2", str(pad_wav),
        ],
        check=True,
    )

    sr, voice_pcm = wavfile.read(str(pad_wav))
    vf = voice_pcm.astype(np.float64) / 32768.0
    if vf.ndim == 1:
        vf = np.stack([vf, vf], axis=1)
    bed = _synthesize_ambient_bed(len(vf), sr)
    mixed = np.clip(vf + bed, -0.98, 0.98)
    wavfile.write(str(mix_wav), sr, (mixed * 32767.0).astype(np.int16))

    # 解析精确句级字幕
    subs = parse_edge_srt(raw_srt, offset_sec=0.4)
    if not subs:
        subs = split_subtitles_fallback(scene["narration"], 0.4, adur)
    else:
        # 句间微调：如果语句被 edge-tts 切得太碎，保留并稍微延长结束缓冲
        subs[-1] = (subs[-1][0], min(dur - 0.1, subs[-1][1] + 0.25), subs[-1][2])
    return mix_wav, adur, dur, subs


def render_scene_pipeline(scene: dict, wav_path: Path, dur: float, subs: list, draw_fn, scratch_dir: Path, data=None) -> Path:
    sid = scene["id"]
    out_mp4 = scratch_dir / f"{sid}.mp4"
    total_frames = int(round(dur * FPS))
    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-f", "rawvideo", "-vcodec", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-i", str(wav_path),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "19",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
        "-shortest", str(out_mp4),
    ]
    t0 = time.time()
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    sub_idx = 0
    for fidx in range(total_frames):
        t = fidx / FPS
        img = BG_IMG.copy()
        d = ImageDraw.Draw(img)
        if data is not None:
            draw_fn(img, d, t, dur, data)
        else:
            draw_fn(img, d, t, dur)
        while sub_idx + 1 < len(subs) and t >= subs[sub_idx][1]:
            sub_idx += 1
        if sub_idx < len(subs) and subs[sub_idx][0] <= t <= subs[sub_idx][1]:
            draw_subtitle(img, subs[sub_idx][2])
        proc.stdin.write(img.tobytes())
    proc.stdin.close()
    rc = proc.wait()
    if rc != 0:
        raise RuntimeError(f"ffmpeg failed for {sid} with code {rc}")
    dt = time.time() - t0
    print(f"[{sid}] {scene['name']} ({scene.get('voice', VOICE_MALE)}): {total_frames}f ({dur:.2f}s) in {dt:.1f}s ({dt/total_frames*1000:.1f}ms/f)", flush=True)
    return out_mp4


def fmt_srt_time(sec: float) -> str:
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_srt_and_meta(meta_list, out_srt: Path, scratch_dir: Path):
    srt_lines, idx, offset = [], 1, 0.0
    for m in meta_list:
        for s0, s1, txt in m["subs"]:
            srt_lines.append(f"{idx}\n{fmt_srt_time(offset + s0)} --> {fmt_srt_time(offset + s1)}\n{txt}\n")
            idx += 1
        offset += m["actual_dur"]
    out_srt.write_text("\n".join(srt_lines), encoding="utf-8")
    (scratch_dir / "meta.json").write_text(json.dumps(meta_list, ensure_ascii=False, indent=2), encoding="utf-8")


def concat_all(mp4_list, out_mp4: Path, scratch_dir: Path):
    list_file = scratch_dir / "concat.txt"
    list_file.write_text("\n".join(f"file '{p}'" for p in mp4_list), encoding="utf-8")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(list_file), "-c", "copy", str(out_mp4)], check=True)
