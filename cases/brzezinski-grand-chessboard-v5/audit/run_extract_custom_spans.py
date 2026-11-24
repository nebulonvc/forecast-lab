"""Brzezinski custom spans (OCR of 上海人民1998中译本; pages separated by \\f): keep 引言(1997年4月) and 第一至七章正文;
drop 封面/版权/中文版序(杨成绪)/卷首语(宋以敏)/目录/地图图表目录 (p1-17) and each chapter's 注 block."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def page_start(text, n):
    pos = 0
    for _ in range(n - 1):
        pos = text.index('\x0c', pos) + 1
    return pos

NOTES = [(57, 58), (91, 92), (131, 132), (177, 179), (217, 218), (268, 271), (299, None)]

def custom_spans(text):
    p18 = page_start(text, 18)
    if not text[p18:p18 + 8].startswith('超级大国政治'):
        raise ValueError(f'intro anchor mismatch {text[p18:p18+8]!r}')
    spans = [(0, p18, 'front_matter:封面/版权/中文版序/卷首语/目录/地图图表目录(1998中译本)')]
    for pg, nxt in NOTES:
        ps = page_start(text, pg)
        m = re.search(r'(^|\n)\s*注\s*[：:]?\s*\n', text[ps:])
        if not m or (nxt and ps + m.start() > page_start(text, nxt)):
            raise ValueError(f'notes not found on p{pg}')
        end = page_start(text, nxt) if nxt else len(text)
        spans.append((ps + m.start() + (1 if m.group(1) else 0), end, f'notes:章末注(p{pg})'))
    return spans

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
