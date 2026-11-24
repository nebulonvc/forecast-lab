"""Run prepare_book.py v5 with book-specific front/back-matter spans.

The default heading detector would:
- treat 序+前言 as front matter and drop the substantive Prologue (前言)
  before 第一章;
- treat 后记/Epilogue as back matter and drop the book's most
  forward-looking chapter (Pacific community, US-China future).

Here we exclude only 序 (acknowledgements and dedication, signed
2011年1月于纽约). 前言 and 后记 are kept.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    intro = text.index('                前言\n')
    return [(0, intro, 'front_matter:序')]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
