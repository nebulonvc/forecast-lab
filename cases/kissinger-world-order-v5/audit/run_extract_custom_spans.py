"""Run prepare_book.py v5 with book-specific front/back-matter spans.

Default heading detection does not match the body markers 「｜第一章｜」,
and treats the endnote heading 「第一章 欧洲：多元化的国际秩序」 at char
228940 as the first chapter. That labels 78% of the file — including the
entire first complete copy (序言 through 结论) — as front matter.

Keep the author 序言, nine chapters and 结论. Exclude the opening 目录
and everything from 致谢 through the notes (and the trailing edit mark)
to EOF.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    preface = text.index('\x0c  序言\n')
    thanks = text.index('\n\n\n  致谢\n') + 3  # start of "  致谢\n"
    if not (800 < preface < 1000 and 226000 < thanks < 228000):
        raise ValueError(f'unexpected heading offsets: preface={preface}, thanks={thanks}')
    return [
        (0, preface, 'front_matter:封面/目录'),
        (thanks, len(text), 'back_matter:致谢/注释'),
    ]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
