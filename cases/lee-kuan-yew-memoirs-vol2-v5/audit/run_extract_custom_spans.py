"""prepare_book.py v5 with book-specific spans for 李光耀回忆录 下卷.
Exclude: TOC and publisher 前言 (before author's 序言); from 李光耀纪事年表 to end
(年表, 鸣谢, 名人读). Keep author's 序言, chapters 1-36 and ch37 后记 (author's)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb
def custom_spans(text):
    pre = text.index('序言\n\n  我的回忆录上册')
    end = text.index('李光耀纪事年表', text.index('37、后记\n\n'))
    return [(0, pre, 'front_matter:目录/出版方前言'), (end, len(text), 'back_matter:年表/鸣谢/名人读')]
pb.matter_spans = custom_spans
if __name__ == '__main__':
    try: sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr); sys.exit(2)
