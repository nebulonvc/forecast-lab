"""Reproduce the limited 1991-2025 US territorial-separation query; stdlib only."""
from pathlib import Path
import csv, hashlib, json
base=Path(__file__).resolve().parent
source=base/'r2-l2-ucdp-acd261.csv'
with source.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f))

def codes(text):
    return {v.strip() for v in text.split(',') if v.strip()}
window=[r for r in rows if 1991 <= int(r['year']) <= 2025]
# Location identifies the country of the incompatibility, NOT battle coordinates.
us_related=[r for r in window if '2' in codes(r['gwno_loc'])]
us_only=[r for r in us_related if codes(r['gwno_loc'])=={'2'}]
intrastate=[r for r in us_only if r['type_of_conflict'] in {'3','4'}]
# Territory or government-and-territory; exclude interstate foreign maritime disputes.
territorial=[r for r in intrastate if r['incompatibility'] in {'1','3'}]
war=[r for r in territorial if r['intensity_level']=='2']
summary=dict(source=source.name,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    version='26.1',source_rows=len(rows),source_years=[min(int(r['year']) for r in rows),max(int(r['year']) for r in rows)],
    observation_years=[1991,2025],us_related_count=len(us_related),us_only_count=len(us_only),
    us_intrastate_count=len(intrastate),territorial_separation_count=len(territorial),territorial_war_count=len(war),
    query='1991<=year<=2025; gwno_loc exactly {2}; type_of_conflict in {3,4}; incompatibility in {1,3}; war subset intensity_level=2',
    geography_limit='location/gwno_loc identify country of incompatibility, not every physical battle location',
    interpretation='No matching US-only intrastate territorial-separation conflict-year, NOT no US war, terrorism, violence or internal conflict.',
    excluded_us_related_rows=us_related,matched_territorial_rows=territorial)
(base/'r2-l2-ucdp-filter-result.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if not isinstance(v,list) or k not in ['excluded_us_related_rows','matched_territorial_rows']},ensure_ascii=False))
