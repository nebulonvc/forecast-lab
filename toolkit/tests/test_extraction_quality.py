import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import prepare_book as pb


def pred(quote,**kw):
    base=dict(quote=quote,kind='prediction',speaker='作者',attribution='author',future_oriented=True,
        claim='c',expanded_claim='e',reference_resolutions=[],unresolved_references=[],time_text='',
        condition_text='',method='m',method_basis='unknown',reason='r')
    base.update(kw);return base


def chunk(text,start=0,end=None,ctx=0):
    end=len(text) if end is None else end
    return dict(id='txt-00001',char_start=start,char_end=end,body=text[start:end],
        context_before=text[max(0,start-ctx):start],context_after=text[end:end+ctx])


class AlignmentTests(unittest.TestCase):
    def test_hard_line_break_and_indent_maps_to_exact_source_span(self):
        text='  美国的价值体系正在衰\n落，整个民主体制也在受到巨大的冲击。\n'
        span=pb.align_quote('美国的价值体系正在衰落，整个民主体制也在受到巨大的冲击。',text)
        self.assertEqual(span['method'],'normalized')
        self.assertEqual(text[span['start']:span['end']],'美国的价值体系正在衰\n落，整个民主体制也在受到巨大的冲击。')

    def test_spaces_around_digits_fullwidth_punctuation_and_quote_marks(self):
        text='到 1990 年，“美国”将会衰落!'
        span=pb.align_quote('到1990年,"美国"将会衰落！',text)
        self.assertEqual(text[span['start']:span['end']],text)

    def test_page_number_line_and_form_feed_inside_quote_are_skipped(self):
        text='这个问题还会长期存\n\n                  37\n\x0c在，并且有恶化的倾向。'
        span=pb.align_quote('这个问题还会长期存在，并且有恶化的倾向。',text)
        self.assertEqual(span['start'],0);self.assertEqual(span['end'],len(text))

    def test_fuzzy_accepts_single_character_slip_and_rejects_paraphrase(self):
        text='如果总统无权组织班子，整个政府如何运转？必定形成互相掣肘和矛盾。'
        span=pb.align_quote('如果总统无权组织班子，整个政府如何运转？必定形成相互掣肘和矛盾。',text)
        self.assertEqual(span['method'],'fuzzy');self.assertEqual(text[span['start']:span['end']],text)
        with self.assertRaisesRegex(ValueError,'not_exact'):
            pb.align_quote('总统没有组班权力会导致政府瘫痪和内耗。',text)

    def test_ambiguous_repeats_prefer_body_or_hint(self):
        text='未来会变化。中间。未来会变化。'
        with self.assertRaisesRegex(ValueError,'ambiguous'):pb.align_quote('未来会变化。',text)
        self.assertEqual(pb.align_quote('未来会变化。',text,prefer=(9,len(text)))['start'],9)
        self.assertEqual(pb.align_quote('未来会变化。',text,hint=9)['start'],9)

    def test_one_bad_quote_no_longer_fails_the_chunk(self):
        text='前文。甲国将\n在明年增加出口。后文。'
        kept,rejected=pb.validate_chunk_predictions(
            [pred('甲国将在明年增加出口。',time_text=None),pred('完全不存在的一句改写的话语内容。')],chunk(text))
        self.assertEqual(len(kept),1);self.assertEqual(rejected[0]['reason'],'quote_not_exact_source_substring')
        self.assertEqual(kept[0]['quote'],'甲国将\n在明年增加出口。')
        self.assertEqual(kept[0]['model_quote'],'甲国将在明年增加出口。')
        self.assertEqual((kept[0]['source_char_start'],kept[0]['source_char_end']),(3,len(text)-3))
        self.assertEqual(kept[0]['time_text'],'')

    def test_quote_from_context_maps_to_global_offsets(self):
        text='上一块的内容。下一块：甲国将增加出口。'
        c=chunk(text,0,7,ctx=20)
        kept,_=pb.validate_chunk_predictions([pred('甲国将增加出口。')],c)
        self.assertEqual(text[kept[0]['source_char_start']:kept[0]['source_char_end']],'甲国将增加出口。')
        self.assertFalse(kept[0]['quote_alignment']['in_body'])

    def test_reference_support_with_line_break_is_kept_and_unsupported_is_set_aside(self):
        text='甲国是讨\n论对象。它将增加出口。'
        p=pred('它将增加出口。',reference_resolutions=[
            dict(expression='它',referent='甲国',support_quote='甲国是讨论对象。'),
            dict(expression='它',referent='乙国',support_quote='乙国是对象。')])
        kept,rejected=pb.validate_chunk_predictions([p],chunk(text))
        self.assertFalse(rejected);self.assertEqual(len(kept[0]['reference_resolutions']),1)
        self.assertEqual(len(kept[0]['unsupported_reference_resolutions']),1)

    def test_missing_unresolved_marker_is_added_visibly(self):
        text='它将增加出口。'
        kept,_=pb.validate_chunk_predictions([pred(text,unresolved_references=['它'])],chunk(text))
        self.assertIn('[指代待确认：它]',kept[0]['expanded_claim'])


class PolicyTests(unittest.TestCase):
    BOOK=('\x0c                   序\n\n  感谢各位。没有他（它）们，本书是不能写成的。\n\n'
          '\x0c             一、不均匀的土地\n  美国的城乡差距今后将会扩大。\n'
          '有人说，“权力的集中化再也不起作用了”。其实不然。\n'
          '一、二千年的传统却又不易反掉。\n'
          '\x0c             后记\n  我相信这本书将来还会再版。\n')

    def test_front_and_back_matter_detection(self):
        spans=pb.matter_spans(self.BOOK)
        self.assertEqual([s[2] for s in spans],['front_matter:序','back_matter:后记'])
        i=self.BOOK.find('本书是不能写成的');self.assertTrue(pb.in_matter(i,i+4,spans))
        j=self.BOOK.find('城乡差距');self.assertIsNone(pb.in_matter(j,j+4,spans))
        k=self.BOOK.find('再版');self.assertTrue(pb.in_matter(k,k+2,spans))
        # a sentence starting with "一、" is not a chapter heading
        self.assertEqual(len([m for m in pb.CHAPTER_HEADING.finditer(self.BOOK)]),1)

    def classify(self,quote,**kw):
        i=self.BOOK.find(quote)
        return pb.classify_prediction(pred(quote,**kw),self.BOOK,i,i+len(quote),pb.matter_spans(self.BOOK))

    def test_acknowledgement_is_excluded(self):
        self.assertEqual(self.classify('没有他（它）们，本书是不能写成的。')[1],'front_or_back_matter')

    def test_rebutted_and_non_future_are_excluded(self):
        self.assertEqual(self.classify('美国的城乡差距今后将会扩大。',attribution='rebutted')[1],'rebutted_or_criticized_view')
        self.assertEqual(self.classify('美国的城乡差距今后将会扩大。',future_oriented=False)[1],'not_future_oriented')

    def test_quoted_text_claimed_as_author_is_demoted(self):
        kind,excluded,flags=self.classify('权力的集中化再也不起作用了')
        self.assertIsNone(excluded);self.assertEqual(kind,'unclear')
        self.assertIn('quoted_text_attributed_to_author',flags)
        self.assertTrue(pb.inside_quotation(self.BOOK,self.BOOK.find('“权力'),self.BOOK.find('”')+1))

    def test_reported_and_missing_attribution_are_demoted_endorsed_kept(self):
        self.assertEqual(self.classify('美国的城乡差距今后将会扩大。',attribution='reported')[0],'unclear')
        self.assertEqual(self.classify('美国的城乡差距今后将会扩大。',attribution=None)[0],'unclear')
        self.assertEqual(self.classify('美国的城乡差距今后将会扩大。',attribution='author_endorsed')[0],'prediction')
        self.assertEqual(self.classify('美国的城乡差距今后将会扩大。')[0],'prediction')

    def test_claims_from_results_applies_policy_and_dedupes_overlaps(self):
        text=self.BOOK;c=chunk(text)
        preds=[pred('美国的城乡差距今后将会扩大。'),pred('美国的城乡差距今后将会扩大'),
               pred('没有他（它）们，本书是不能写成的。'),pred('权力的集中化再也不起作用了')]
        kept,_=pb.validate_chunk_predictions(preds,c)
        report={}
        claims=pb.claims_from_results([dict(id=c['id'],predictions=kept)],[c],text,'0'*64,{},None,report)
        self.assertEqual([x['kind'] for x in claims],['prediction','unclear'])
        self.assertEqual(report['duplicates'],1)
        self.assertEqual([e['reason'] for e in report['excluded']],['front_or_back_matter'])
        for x in claims:
            loc=x['source_location'];self.assertEqual(text[loc['char_start']:loc['char_end']],x['quote'])

    def test_prompt_requests_attribution_and_excludes_front_matter(self):
        self.assertIn('attribution',pb.DISCOVER_PROMPT);self.assertIn('rebutted',pb.DISCOVER_PROMPT)
        self.assertIn('致谢',pb.DISCOVER_PROMPT);self.assertIn('future_oriented',pb.DISCOVER_PROMPT)
        self.assertEqual(pb.DISCOVER_PROMPT,pb.DISCOVER_PROMPT_V5)
        self.assertIn('claim_type',pb.DISCOVER_PROMPT);self.assertNotIn('claim_type',pb.DISCOVER_PROMPT_V4)


if __name__=='__main__':unittest.main()
