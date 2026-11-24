"""Run prepare_book.py v5 with book-specific front/back-matter spans.

The default heading detector misfires on this book: TOC lines such as
「第一部分 中国的崛起」are treated as the first chapter, so the real
「前言」is labelled back matter and cuts off most of the 引言 (chars
5620-17091). The 推荐序 is left in. Here we exclude only 目录/推荐序/
前言/致谢 (before 引言) and 附录1/附录2 at the end. 引言, ten chapters
and 结论 are kept.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    intro = text.index('\n               引 言\n') + 1
    appendix = text.index('\n     附录 1   修昔底德陷阱案例文件\n') + 1
    if not (10000 < intro < 20000 and 170000 < appendix < 190000):
        raise ValueError(f'unexpected heading offsets: intro={intro}, appendix={appendix}')
    return [
        (0, intro, 'front_matter:目录/推荐序/前言/致谢'),
        (appendix, len(text), 'back_matter:附录1/附录2'),
    ]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
