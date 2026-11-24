"""Run prepare_book.py v5 with book-specific spans for an incomplete TXT.

The TXT is a sample-style file: body has ch.1-2, part of ch.3 ('样章到此结束'),
then jumps into the second half of ch.9, then 后记 and 附录, then ~200K chars
of 注释 whose headings look like chapters. Default detection would drop the
author's 前言 and treat 后记 as back matter through to ch.1, and it would keep
the notes. We exclude: promo/摘要/赞誉/译者序 (before 前言), 致谢/作者简介,
the resources page before 附录, and all 注释.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'toolkit'))
import prepare_book as pb

def custom_spans(text):
    preface = text.index('前言', 6000)
    preface = text.rfind('\x0c', 0, preface)
    ack = text.index('致谢', preface)
    ack = text.rfind('\x0c', 0, ack)
    ch1 = text.index('第1章   六大纪元')
    ch1 = text.rfind('\x0c', 0, ch1)
    res = text.index('本书相关资源与联系信息', 109000)
    res = text.rfind('\x0c', 0, res)
    app = text.index('附录   重新审视加速回归定律')
    app = text.rfind('\x0c', 0, app)
    notes = text.index('注释\n前言')
    notes = text.rfind('\x0c', 0, notes)
    return [(0, preface, 'front_matter:宣传页/摘要/赞誉/译者序'),
            (ack, ch1, 'front_matter:致谢/作者简介'),
            (res, app, 'back_matter:本书相关资源与联系信息'),
            (notes, len(text), 'back_matter:注释')]

pb.matter_spans = custom_spans
if __name__ == '__main__':
    try:
        sys.exit(pb.main())
    except (ValueError, OSError) as exc:
        print('Preparation stopped: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        sys.exit(2)
