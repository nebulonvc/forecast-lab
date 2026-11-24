"""Soros custom spans: keep 1987 导论, ch.1-19 and 结束语; drop later-edition material."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    intro = text.index('导\u3000\u3000\u3000\u3000论\n')
    pref94 = text.index('前\u3000\u3000言\n')
    part1 = text.index('\x0c第一部分\u3000\u3000理论\n') + 1
    ch20 = text.index('第二十章\u3000\u3000１９８７ 年大崩盘\n')
    epi = text.index('结束语\n', ch20)
    # back up to line starts
    intro = text.rfind('\n', 0, intro) + 1; pref94 = text.rfind('\n', 0, pref94) + 1
    ch20 = text.rfind('\n', 0, ch20) + 1; epi = text.rfind('\n', 0, epi) + 1
    if not (0 < intro < 1000 and 9000 < pref94 < 11000 and 19000 < part1 < 20000 and 255000 < ch20 < epi < 275000):
        raise ValueError(f'unexpected offsets {intro} {pref94} {part1} {ch20} {epi}')
    return [
        (0, intro, 'front_matter:中文版出版社简介'),
        (pref94, part1, 'front_matter:1994前言/原序(Tudor Jones)/1999译序'),
        (ch20, epi, 'later_edition:第二十章1987年大崩盘(1988年平装本新增)'),
    ]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
