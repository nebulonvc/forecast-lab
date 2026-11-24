"""Kennedy custom spans (OCR text, pages separated by \\f): keep 引言(p6-17), 第一至八章 and 后记(原书 Epilogue);
drop 封面/书名页/版权页/译者的话(p1-5) and 目录(p18-19)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def page_start(text, n):  # 1-based page n -> char offset
    pos = 0
    for _ in range(n - 1):
        pos = text.index('\x0c', pos) + 1
    return pos

def custom_spans(text):
    p6, p18, p20 = page_start(text, 6), page_start(text, 18), page_start(text, 20)
    if not (text[p6:p6+12].startswith('本书是论述') and text[p18:p18+4].startswith('第一编') and '第一编' in text[p20:p20+20]):
        raise ValueError(f'unexpected page anchors {text[p6:p6+12]!r} {text[p18:p18+8]!r} {text[p20:p20+12]!r}')
    return [
        (0, p6, 'front_matter:封面/书名页/版权页/译者的话(1988中译本)'),
        (p18, p20, 'front_matter:目录'),
    ]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
