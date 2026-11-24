"""Run prepare_book.py v5 with book-specific front/back-matter spans.

The default heading detector misfires on this book: the TOC's 致谢 line marked
中文版序 + 如何阅读本书 + 引言 as back matter, and the per-chapter 附录 heading
in chapter 2 excluded chapters 3-7 (chars 43014-132996). Here we exclude only
中文版序/如何阅读本书 (before 引言) and 致谢/审校后记 at the end. 引言 and the
computer-analysis appendix are kept.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    intro = text.index('\n\x0c                引言\n') + 1
    ack = text.index('\x0c                致谢\n   衷心感谢')
    return [(0, intro, 'front_matter:目录/中文版序/如何阅读本书'), (ack, len(text), 'back_matter:致谢/审校后记')]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try: sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr); sys.exit(2)
