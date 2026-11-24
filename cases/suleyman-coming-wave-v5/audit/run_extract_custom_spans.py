"""Run prepare_book.py v5 with book-specific spans.

Default detection drops everything before 第一章 (correct here, since the
short 前言 is explicitly AI-generated text, not the authors' own claims) but
only drops 致谢 at the end, leaving the 注释 section whose per-chapter
headings look like real chapters. We exclude front matter through 前言 and
everything from 致谢 to the end (致谢 + 注释).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    ch1 = text.index('\x0c  第一章\n\n遏制是不可能的')
    ack = text.index('\x0c                     致谢\n')
    return [(0, ch1, 'front_matter:版权/赞誉/推荐序/AI生成前言'), (ack, len(text), 'back_matter:致谢/注释')]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
