"""Run prepare_book.py v5 with book-specific spans.

The TXT has only a TOC at the top (chapter headings do not reappear in the
body) plus many homeofpdf watermark lines. Default detection finds no matter
spans and would keep the TOC and the final 致谢. We exclude the TOC before
作者序 and the 致谢 at the end; the author's preface and all body text are kept.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    pre = text.index('作者序')
    pre = text.rfind('\x0c', 0, pre)
    ack = text.rindex('   致谢\n')
    return [(0, pre, 'front_matter:水印/目录'), (ack, len(text), 'back_matter:致谢')]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
