import contextlib
import csv
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import prepare_book as pb
import pipeline


def prediction():
    return dict(quote='它将在明年增加出口。',kind='prediction',speaker='作者',
        claim='增加出口',expanded_claim='甲国将在明年增加出口。',
        reference_resolutions=[dict(expression='它',referent='甲国',support_quote='甲国是讨论对象。')],
        unresolved_references=[],time_text='明年',condition_text='',method='原文未提供推理',
        method_basis='unknown',reason='对未来出口的判断')


class TxtTests(unittest.TestCase):
    def test_decode_encodings_and_reject_wrong_encoding(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/'book.txt'
            for codec,explicit in [('utf-8-sig',None),('utf-16',None),('gb18030','gb18030')]:
                path.write_bytes('甲国\r\n未来'.encode(codec))
                self.assertEqual(pb.decode_text(path,explicit)[1],'甲国\r\n未来')
            with self.assertRaises(ValueError):pb.decode_text(path)
            path.write_text(' \n')
            with self.assertRaisesRegex(ValueError,'empty'):pb.decode_text(path)

    def test_chunks_cover_all_characters_with_context_and_real_lines(self):
        text='甲国。\r\n' * 120
        chunks=pb.split_text(text,200,30)
        self.assertEqual(''.join(c['body'] for c in chunks),text)
        self.assertGreater(len(chunks),1)
        for c in chunks:
            self.assertEqual(c['body'],text[c['char_start']:c['char_end']])
            self.assertEqual(c['line_start'],text[:c['char_start']].count('\n')+1)
        self.assertEqual(chunks[1]['context_before'],text[chunks[1]['char_start']-30:chunks[1]['char_start']])

    def test_exact_quote_and_duplicate_offset(self):
        with self.assertRaisesRegex(ValueError,'not_exact'):pb.quote_offset({'quote':'改写'},'原文')
        with self.assertRaisesRegex(ValueError,'ambiguous'):pb.quote_offset({'quote':'未来'},'未来，未来')
        self.assertEqual(pb.quote_offset({'quote':'未来','quote_start':3},'未来，未来'),3)
        with self.assertRaisesRegex(ValueError,'mismatch'):pb.quote_offset({'quote':'未来','quote_start':2},'未来，未来')

    def test_whitespace_alignment_restores_exact_source_span(self):
        text='甲国是讨论\n对象。它将在明年\r\n增加出口。'
        chunks=pb.split_text(text)
        pred=prediction();pred['quote_start']=0
        pred['reference_resolutions'][0]['expression']='它\n将在'
        raw={'choices':[{'finish_reason':'stop','message':{'content':json.dumps({'items':[
            dict(id=chunks[0]['id'],predictions=[pred])]})}}]}
        original=json.dumps(raw)
        result=pb.validate_result('discover',raw,chunks)
        fixed=result[0]['predictions'][0]
        self.assertEqual(fixed['quote'],'它将在明年\r\n增加出口。')
        self.assertEqual(fixed['quote_alignment']['method'],'normalized')
        self.assertEqual(fixed['reference_resolutions'][0]['support_quote'],'甲国是讨论对象。')
        self.assertEqual(json.dumps(raw),original)
        claims=pb.claims_from_results(result,chunks,text,hashlib.sha256(text.encode()).hexdigest(),{'book':'测试'})
        start=claims[0]['source_location']['char_start']
        end=claims[0]['source_location']['char_end']
        self.assertEqual(text[start:end],fixed['quote'])
        self.assertIn('provenance',claims[0]['extraction_v2'])

    def test_whitespace_alignment_rejects_ambiguous_and_unrelated_quotes(self):
        with self.assertRaisesRegex(ValueError,'ambiguous'):
            pb.align_quote('未 来','未来，未\n来')
        raw_quote='这只是正文。'
        text='甲国是讨论对象。它将在明年增加出口。'
        chunks=pb.split_text(text)
        pred=prediction();pred['quote']=raw_quote
        raw={'choices':[{'finish_reason':'stop','message':{'content':json.dumps({'items':[
            dict(id=chunks[0]['id'],predictions=[pred])]})}}]}
        result=pb.validate_result('discover',raw,chunks)
        self.assertEqual(result[0]['predictions'],[])
        self.assertEqual(result[0]['rejected_predictions'][0]['reason'],'quote_not_exact_source_substring')

    def test_expansion_requires_source_support_and_visible_uncertainty(self):
        item=prediction()
        pb.validate_expansion(item,'甲国是讨论对象。它将在明年增加出口。')
        with self.assertRaisesRegex(ValueError,'not_in_source'):pb.validate_expansion(item,'它将在明年增加出口。')
        item.update(reference_resolutions=[],unresolved_references=['它'])
        with self.assertRaisesRegex(ValueError,'visible_marker'):pb.validate_expansion(item,item['quote'])
        item['expanded_claim']='[指代待确认：它]将在明年增加出口。'
        pb.validate_expansion(item,item['quote'])

    def test_mocked_txt_import_and_report_keep_quote_and_line_location(self):
        with tempfile.TemporaryDirectory() as folder,contextlib.redirect_stdout(io.StringIO()):
            root=Path(folder)/'case';source=Path(folder)/'book.txt'
            pipeline.main(['--case',str(root),'init','--book','测试','--publication-year','2020','--cutoff','2026-11-08'])
            source.write_bytes('甲国是讨论对象。\r\n它将在明年增加出口。\r\n'.encode())
            key=Path(folder)/'secret.key';key.write_text('test-secret')
            def opener(request,timeout):
                body=json.loads(request.data);data=json.loads(body['messages'][1]['content'])
                items=[dict(id=c['id'],predictions=[prediction()]) for c in data['cases']]
                raw={'choices':[{'finish_reason':'stop','message':{'content':json.dumps({'items':items})}}],
                     'usage':{'prompt_tokens':100,'completion_tokens':100,'total_tokens':200}}
                response=io.BytesIO(json.dumps(raw).encode())
                return response
            with patch.object(pb.rp.urllib.request,'urlopen',side_effect=opener) as network:
                status=pb.main(['--case',str(root),'txt',str(source),'--key-file',str(key),'--apply'])
                self.assertEqual(status,0);self.assertEqual(network.call_count,1)
                with self.assertRaisesRegex(ValueError,'empty case'):
                    pb.main(['--case',str(root),'txt',str(source),'--key-file',str(key),'--apply'])
                self.assertEqual(network.call_count,1)
            rows=pb.rp.read_jsonl(root/'data/claims.jsonl');self.assertEqual(len(rows),1)
            claim=rows[0];self.assertIsNone(claim['page'])
            cfg=pb.rp.read_json(root/'config.json')
            pb.validate_extraction_provenance(claim,cfg)
            checkpoints=list((root/'output/txt_import/checkpoints').glob('*/*.json'))
            self.assertEqual(len(checkpoints),1)
            self.assertEqual(pb.rp.read_json(checkpoints[0])['claims'],rows)
            self.assertEqual(claim['source_location']['line_start'],2)
            self.assertEqual(claim['source_location']['line_end'],2)
            self.assertEqual(claim['source_verification']['sha256'],hashlib.sha256(source.read_bytes()).hexdigest())
            self.assertEqual(claim['quote'],prediction()['quote'])
            pipeline.main(['--case',str(root),'check']);pipeline.main(['--case',str(root),'report'])
            report=(root/'output/report.md').read_text()
            self.assertIn('TXT 第 2 行',report);self.assertIn('扩展观点（解释，非原文）：甲国',report)
            with (root/'output/claims.csv').open(encoding='utf-8-sig') as handle:
                row=next(csv.DictReader(handle))
                self.assertEqual(row['pdf_page'],'');self.assertEqual(row['line_start'],'2')
                self.assertEqual(row['expanded_claim'],prediction()['expanded_claim'])

    def test_provenance_rejects_changed_source_rules_or_extraction(self):
        text='甲国是讨论对象。它将在明年增加出口。'
        chunks=pb.split_text(text)
        cfg={'book':'测试','rules_version':'v1'}
        def claim():
            return pb.claims_from_results([dict(id=chunks[0]['id'],predictions=[prediction()])],
                chunks,text,hashlib.sha256(text.encode()).hexdigest(),cfg)[0]
        pb.validate_extraction_provenance(claim(),cfg)
        for field,value in [('context','改变的上下文'),('speaker','另一人'),('source_verified',False)]:
            changed=claim();changed[field]=value
            with self.assertRaises(ValueError):pb.validate_extraction_provenance(changed,cfg)
        changed=claim();changed['extraction_v2']['claim']='另一个判断'
        with self.assertRaisesRegex(ValueError,'provenance_mismatch'):
            pb.validate_extraction_provenance(changed,cfg)
        with self.assertRaisesRegex(ValueError,'provenance_mismatch'):
            pb.validate_extraction_provenance(claim(),dict(cfg,rules_version='v2'))

    def test_reused_extraction_remains_reusable_after_full_import(self):
        with tempfile.TemporaryDirectory() as folder,contextlib.redirect_stdout(io.StringIO()):
            root=Path(folder)/'case'
            pipeline.main(['--case',str(root),'init','--book','测试','--publication-year','2020','--cutoff','2026-11-08'])
            cfg=pb.rp.read_json(root/'config.json')
            text='甲国是讨论对象。它将在明年增加出口。'
            chunks=pb.split_text(text)
            claims=pb.claims_from_results([dict(id=chunks[0]['id'],predictions=[prediction()])],
                chunks,text,hashlib.sha256(text.encode()).hexdigest(),cfg)
            pb.rp.save_jsonl(root/'data/claims.jsonl',claims)
            _,before=pb.rp.prepare_batches(root,assess_only=True)
            proposal=root/'output/reused_extract.jsonl'
            pb.rp.save_jsonl(proposal,[c['extraction'] for _,_,batch in before for c in batch['cases']])
            pipeline.main(['--case',str(root),'apply','extract-full',str(proposal)])
            imported=pb.rp.read_jsonl(root/'data/claims.jsonl')
            self.assertIn('receipt',imported[0]['extraction_v2'])
            self.assertEqual(imported[0]['extraction_v2']['provenance'],claims[0]['extraction_v2']['provenance'])
            _,after=pb.rp.prepare_batches(root,assess_only=True)
            self.assertEqual(before,after)
            for field in ('claim','expanded_claim','condition_text'):
                changed=json.loads(json.dumps(imported))
                changed[0]['extraction_v2'][field]='另一个判断'
                pb.rp.save_jsonl(root/'data/claims.jsonl',changed)
                with self.subTest(field=field),self.assertRaisesRegex(ValueError,'provenance_mismatch'):
                    pb.rp.prepare_batches(root,assess_only=True)

    def test_checkpoint_ready_before_slow_failed_segment_without_partial_import(self):
        with tempfile.TemporaryDirectory() as folder,contextlib.redirect_stdout(io.StringIO()):
            root=Path(folder)/'case';source=Path(folder)/'book.txt'
            text='甲国是讨论对象。它将在明年增加出口。'+'甲'*180+'。'+'乙'*190+'。'
            source.write_text(text)
            pipeline.main(['--case',str(root),'init','--book','测试','--publication-year','2020','--cutoff','2026-11-08'])
            key=Path(folder)/'secret.key';key.write_text('test-secret')
            ready=threading.Event();save=pb.rp.save_json
            def save_checkpoint(path,value):
                save(path,value)
                if Path(path).name=='txt-00001.json':ready.set()
            def opener(request,timeout):
                data=json.loads(json.loads(request.data)['messages'][1]['content'])
                c=data['cases'][0]
                if c['id']!='txt-00001':
                    self.assertTrue(ready.wait(5),'first segment was not handed off while another request waited')
                    self.assertEqual((root/'data/claims.jsonl').read_text(),'')
                    raise RuntimeError('simulated request failure')
                raw={'choices':[{'finish_reason':'stop','message':{'content':json.dumps({'items':[
                    dict(id=c['id'],predictions=[prediction()])]})}}],
                    'usage':{'prompt_tokens':100,'completion_tokens':100,'total_tokens':200}}
                return io.BytesIO(json.dumps(raw).encode())
            with patch.object(pb.rp,'save_json',side_effect=save_checkpoint),patch.object(pb.rp.urllib.request,'urlopen',side_effect=opener):
                self.assertEqual(pb.main(['--case',str(root),'txt',str(source),'--chunk-chars','200',
                    '--workers','2','--key-file',str(key),'--apply']),2)
            self.assertTrue(ready.is_set())
            self.assertEqual((root/'data/claims.jsonl').read_text(),'')
            checkpoint=pb.rp.read_json(next((root/'output/txt_import/checkpoints').glob('*/txt-00001.json')))
            self.assertFalse(checkpoint['full_book_complete'])
            self.assertEqual(checkpoint['claims'][0]['quote'],prediction()['quote'])
            summary=pb.rp.read_json(root/'output/txt_import/summary.json')
            self.assertFalse(summary['complete']);self.assertFalse(summary['imported'])

    def test_resume_rebuilds_same_checkpoint_from_cache_without_paid_request(self):
        with tempfile.TemporaryDirectory() as folder,contextlib.redirect_stdout(io.StringIO()):
            root=Path(folder)/'case';source=Path(folder)/'book.txt'
            source.write_text('甲国是讨论对象。它将在明年增加出口。')
            pipeline.main(['--case',str(root),'init','--book','测试','--publication-year','2020','--cutoff','2026-11-08'])
            key=Path(folder)/'secret.key';key.write_text('test-secret')
            raw={'choices':[{'finish_reason':'stop','message':{'content':json.dumps({'items':[
                dict(id='txt-00001',predictions=[prediction()])]})}}],
                'usage':{'prompt_tokens':100,'completion_tokens':100,'total_tokens':200}}
            args=['--case',str(root),'txt',str(source),'--key-file',str(key)]
            with patch.object(pb.rp.urllib.request,'urlopen',return_value=io.BytesIO(json.dumps(raw).encode())) as network:
                self.assertEqual(pb.main(args),0);self.assertEqual(network.call_count,1)
            path=next((root/'output/txt_import/checkpoints').glob('*/*.json'))
            before=path.read_bytes();path.unlink()
            with patch.object(pb.rp.urllib.request,'urlopen',side_effect=AssertionError('duplicate paid call')):
                self.assertEqual(pb.main(args+['--apply']),0)
            self.assertEqual(path.read_bytes(),before)
            self.assertEqual(pb.rp.read_jsonl(root/'data/claims.jsonl'),pb.rp.read_json(path)['claims'])

    def test_prepare_only_requires_no_key_and_makes_no_network_calls(self):
        with tempfile.TemporaryDirectory() as folder,contextlib.redirect_stdout(io.StringIO()):
            root=Path(folder)/'case';source=Path(folder)/'book.txt';source.write_text('未来会变化。')
            pipeline.main(['--case',str(root),'init','--book','测试','--publication-year','2020','--cutoff','2026-11-08'])
            with patch.object(pb.rp.urllib.request,'urlopen',side_effect=AssertionError('network called')):
                self.assertEqual(pb.main(['--case',str(root),'txt',str(source),'--prepare-only']),0)
            self.assertEqual((root/'data/claims.jsonl').read_text(),'')
            self.assertTrue((root/'output/txt_import/manifest.json').exists())

    def test_expansion_import_preserves_assessment_and_handles_blank_quotes(self):
        with tempfile.TemporaryDirectory() as folder,contextlib.redirect_stdout(io.StringIO()):
            root=Path(folder)/'case'
            pipeline.main(['--case',str(root),'init','--book','测试','--publication-year','2020','--cutoff','2026-11-08'])
            assessment={'verdict':'暂无法判断','reason':'原始判定'}
            original=[dict(id='a',quote='它将在明年增加出口。',context='甲国是讨论对象。',assessment=assessment,
                           extraction_v2={'kind':'unclear','claim':'原始摘要'}),
                      dict(id='blank',quote='',assessment=None)]
            pb.rp.save_jsonl(root/'data/claims.jsonl',original)
            def call(runner,stage,request,group,n):
                self.assertEqual(stage,'expand')
                self.assertNotIn('assessment',json.loads(request['messages'][1]['content'])['cases'][0])
                return [dict(id='a',**prediction())]
            with patch.object(pb.rp.Runner,'call',call),patch.dict('os.environ',{'DEEPSEEK_API_KEY':'test'}):
                self.assertEqual(pb.main(['--case',str(root),'expand','--apply']),0)
            updated=pb.rp.read_jsonl(root/'data/claims.jsonl')
            self.assertEqual(updated[0]['assessment'],assessment)
            self.assertEqual(updated[0]['quote'],original[0]['quote'])
            self.assertEqual(updated[0]['extraction_v2']['kind'],'unclear')
            self.assertEqual(updated[0]['extraction_v2']['claim'],'原始摘要')
            self.assertEqual(updated[1],original[1])


if __name__=='__main__':unittest.main()
