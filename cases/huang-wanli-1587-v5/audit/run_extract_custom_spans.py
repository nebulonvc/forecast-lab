"""Wanli custom spans: keep 自序 + ch.1-7; drop TOC and appendices."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    pre = text.index('\x0c                       自 序\n')
    app = text.index('\x0c              附录')
    if not (200 < pre < 400 and 170000 < app < 180000):
        raise ValueError(f'unexpected offsets {pre} {app}')
    return [(0, pre, 'front_matter:目录'), (app, len(text), 'back_matter:附录一(史料)/附录二(后写文章)')]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
