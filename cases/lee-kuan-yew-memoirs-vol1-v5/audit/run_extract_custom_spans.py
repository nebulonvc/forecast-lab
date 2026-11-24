"""prepare_book.py v5 with book-specific spans for 李光耀回忆录 上卷.
Exclude: the leading TOC (before 序言); from 李光耀纪事年表 to end (年表, 鸣谢,
华文版说明, 简体版编者后记, repeated TOC). Keep author's 序言 and chapters 1-42."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb
def custom_spans(text):
    pre = text.index('序言\n从来没打算写回忆录')
    end = text.index('李光耀纪事年表\n1923')
    return [(0, pre, 'front_matter:目录'), (end, len(text), 'back_matter:年表/鸣谢/后记/目录')]
pb.matter_spans = custom_spans
if __name__ == '__main__':
    try: sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr); sys.exit(2)
