"""Mearsheimer custom spans (OCR of 上海人民2003中译本 of the 2001 original; pages separated by \\f).
Keep 英文版前言 (original 2001 preface) and 第一至十章 body text; drop 2002-03 Chinese-edition material
(倪世雄序, 王义桅书评, 2002-04-22 中文版前言), 致谢/目录, each chapter's endnotes, and 译后记."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def page_start(text, n):
    pos = 0
    for _ in range(n - 1):
        pos = text.index('\x0c', pos) + 1
    return pos

# (notes page, anchor) -> notes run until next chapter start page
NOTES = [(78, None, 93), (117, None, 130), (155, None, 171), (222, None, 253), (280, '\n1．我提醒读者', 295),
         (358, None, 391), (420, None, 438), (501, None, 528), (552, '\n1. G. Iowes Dickinson', 557), (596, None, 617)]

def custom_spans(text):
    p45, p48, p52, p617 = (page_start(text, n) for n in (45, 48, 52, 617))
    for pos, want in ((p45, '英文版前言'), (p48, '致谢'), (p617, '译后记')):
        if not text[pos:pos + 10].startswith(want):
            raise ValueError(f'anchor mismatch {want} {text[pos:pos+10]!r}')
    if '导论' not in text[p52:p52 + 10]:
        raise ValueError('ch1 anchor mismatch')
    spans = [(0, p45, 'front_matter:封面/CIP/倪世雄序(2002)/王义桅书评/中文版前言(2002-04-22)'),
             (p48, p52, 'front_matter:致谢/目录')]
    for pg, anchor, nxt in NOTES:
        ps, pe = page_start(text, pg), page_start(text, pg + 1) - 1
        page = text[ps:pe]
        if anchor:
            k = page.index(anchor) + 1
        else:
            m = re.search(r'(^|\n)注\s*释\n', page)
            if not m: raise ValueError(f'notes header not found on p{pg}')
            k = m.start() + (1 if m.group(1) else 0)
        spans.append((ps + k, page_start(text, nxt), f'notes:章末注释(p{pg}-{nxt-1})'))
    spans.append((p617, len(text), 'back_matter:译后记'))
    return spans

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
