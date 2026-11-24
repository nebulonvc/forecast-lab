"""Kurzweil custom spans: keep Introduction + ch.1-8; drop front matter and appendix/notes/index/about-the-author."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    intro = text.index('\x0cI\nINTRODUCTION\nn my 2005 book') + 1
    appx = text.index('RAY: That we agree on.\x0cAPPENDIX\n') + len('RAY: That we agree on.')
    if not (4000 < intro < 8000 and 540000 < appx < 560000):
        raise ValueError(f'unexpected offsets {intro} {appx}')
    return [
        (0, intro, 'front_matter:书名页/版权/目录/献词/致谢'),
        (appx, len(text), 'back_matter:附录(价格性能数据方法)/注释/索引/作者简介'),
    ]

pb.matter_spans = custom_spans

# English-language source: the toolkit's deterministic screens are Chinese-only regexes, so every English
# quote failed stated_change() and was demoted to unclear. Add English equivalents (original Chinese kept).
import re as _re
_I = _re.IGNORECASE
pb._FUTURE_WINDOW = _re.compile(pb._FUTURE_WINDOW.pattern + r"|\bnext (?:year|decade|few (?:years|decades))\b|\bin the (?:coming|next) (?:\w+ )?(?:years?|decades?|century)\b|\bby (?:the (?:end|middle) of )?(?:the )?(?:19|20)\d{2}s?\b|\bby the (?:early |mid-|late )?(?:19|20)\d0s\b|\bwithin (?:the next )?(?:a |\w+ )?(?:years?|decades?)\b|\b(?:in|over) the (?:near |long-term |distant )?future\b|\bdecades? (?:ahead|from now)\b|\bby mid-century\b|\bin the long (?:run|term)\b|\bsoon\b|\beventually\b", _I)
pb._OPERATIONAL_HORIZON = _re.compile(pb._OPERATIONAL_HORIZON.pattern + r"|\bnext year\b|\bby (?:the (?:end|middle) of )?(?:the )?(?:19|20)\d{2}s?\b|\bby the (?:early |mid-|late )?(?:19|20)\d0s\b|\bwithin (?:the next )?(?:a |\w+ )?(?:years?|decades?)\b|\bin the (?:coming|next) (?:\w+ )?(?:years?|decades?)\b", _I)
pb._CHANGE = _re.compile(pb._CHANGE.pattern + r"|\bwill\b|\bwon't\b|\bgoing to\b|\blikely\b|\bmay\b|\bmight\b|\bincreas\w*|\bdecreas\w*|\bdeclin\w*|\brise\b|\brising\b|\bgrow\w*|\bexpand\w*|\bshrink\w*|\breplac\w*|\bbecom\w*|\baccelerat\w*|\bimprov\w*|\bworsen\w*|\bsurpass\w*|\bexceed\w*|\bdoubl\w*|\bfall\b|\bdrop\w*|\bcollaps\w*|\btransform\w*", _I)
pb._FUTURE_MODAL = _re.compile(pb._FUTURE_MODAL.pattern + r"|\bwill\b|\bwon't\b|\bgoing to\b|\blikely\b|\bmay\b|\bmight\b", _I)
pb._ADVICE = _re.compile(pb._ADVICE.pattern + r"|\bshould\b|\bought to\b|\bwe must\b|\bneed to\b", _I)
pb._MECH = _re.compile(pb._MECH.pattern + r"|\bbecause\b|\bdue to\b|\bleads? to\b|\bcaused by\b|\bthe reason\b", _I)
pb._PAST = _re.compile(pb._PAST.pattern + r"|\bpreviously\b|\bhistorically\b|\bat that time\b|\bwas the result\b", _I)
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
