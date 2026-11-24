"""Harari custom spans (cleaned OCR of 中信2017中译本 scan; pages separated by \\f): keep 第1-11章 incl. part
openers and closing section; drop 封面/目录/卷首插图 (p1-5). Scan has no 注释/致谢/索引/译者序."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def page_start(text, n):
    pos = 0
    for _ in range(n - 1):
        pos = text.index('\x0c', pos) + 1
    return pos

def custom_spans(text):
    p6 = page_start(text, 6)
    if not text[p6:p6 + 20].startswith('1第1章】\n人类的新议题'):
        raise ValueError(f'ch1 anchor mismatch {text[p6:p6+20]!r}')
    return [(0, p6, 'front_matter:封面/目录/卷首插图')]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
