"""Run prepare_book.py v5 with book-specific front/back-matter spans.

Default heading detection treats the TOC '第一章' as the first chapter, then
treats the TOC '致谢' as back matter and drops 重磅推荐, 推荐序 and the
2021 Chinese-edition preface (signed 2021-04-05). It would also be unsafe
to keep the end-matter 附录, which reprints Stephen Walt's essay rather than
Mahbubani's own forecasts.

We exclude: 目录/重磅推荐/推荐序/中文版序言 (before 第一章), and
致谢/附录/版权页 at the end. Chapters 1-9 are kept.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    ch1 = text.index('\x0c   第一章\n')
    ack = text.index('\x0c                致谢\n')
    return [
        (0, ch1, 'front_matter:目录/重磅推荐/推荐序/中文版序言'),
        (ack, len(text), 'back_matter:致谢/附录/版权页'),
    ]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
