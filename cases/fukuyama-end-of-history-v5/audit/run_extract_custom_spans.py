"""Run prepare_book.py v5 with book-specific front/back-matter spans.

Default detection already drops the 2014 新版序 and 1992 代序 (mislabeled
as back matter between the TOC 参考文献 and 第一部分) and drops the 2006
附录 afterword. It also keeps a sliver of the TOC. Custom spans are
clearer and avoid depending on that accident: exclude everything before
the body 「第一部分」, and exclude 「附录」/参考文献/致谢 to EOF.
Keep all 31 chapters (第1章 through 第31章).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    part1 = text.index('\x0c                                     第一部分\n')
    appendix = text.index('\x0c                                        附录\n')
    if not (30000 < part1 < 40000 and 420000 < appendix < 440000):
        raise ValueError(f'unexpected heading offsets: part1={part1}, appendix={appendix}')
    return [
        (0, part1, 'front_matter:总序/导读/目录/2014新版序/1992代序'),
        (appendix, len(text), 'back_matter:附录（2006后记）/参考文献/致谢'),
    ]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
