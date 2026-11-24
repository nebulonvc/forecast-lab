"""Run prepare_book.py v5 with book-specific spans.

Default detection treats the TOC '致谢' line as back matter and drops the
authors' 前言 (dedication through the start of 第一章). We exclude only the
cover/TOC/dedication before 前言 and the final 致谢 + copyright page.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    preface = text.index('\x0c               前言\n')
    ack = text.rindex('\x0c              致谢\n')
    return [(0, preface, 'front_matter:封面/目录/献辞'), (ack, len(text), 'back_matter:致谢/版权页')]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
