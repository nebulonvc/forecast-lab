"""Run prepare_book.py v5 with book-specific front/back-matter spans.

Default heading detection treats 前言 as the start of front matter and
extends that span through the end of the preface, dropping Mahbubani's
own 前言. It also does not treat 附录 or 译后记 as back matter.

The Chinese text includes a 推荐序 signed 「2023年4月于北京」 (after
the English 2021-12-30 publication), which must be excluded. The end
附录 is a bibliography of Mahbubani's earlier books, followed by the
translator's afterword.

We exclude: 推荐序 (chars 0 to 前言), and 附录+译后记 at the end.
The author's 前言 and Parts 1-4 are kept.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    preface = text.index('\x0c前言\n')
    appendix = text.index('\x0c附录    马凯硕著作简介\n')
    return [
        (0, preface, 'front_matter:推荐序（2023年4月）'),
        (appendix, len(text), 'back_matter:附录/译后记'),
    ]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
