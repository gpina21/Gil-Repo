"""Backtest: how should the card's "Top assist plays" (top 3) be ranked?

Reads the NBA Prop Model card's saved HTML (or its extracted DATA JSON), takes every
graded Early assist paper play (first posted price, 1u flat, one play per game), and
compares top-3 rankings: the current gap %, EV and hit chance from the plain projection,
assist cushion, and the card's own EV/edge. Also prints the full Early list split by
priced-in, results by line bucket, and rebound results by line (the 4.5-6.5 window).

Usage:  python3 nba/top3_backtest.py <card.html | data.json>

First run Nov 23 2026 (Nov 11-22, 12 nights): no ranking clearly beat the current one;
decision was to wait for more nights, rerun, then decide.
"""
import json,sys
from collections import defaultdict

def load(path):
    t=open(path,encoding='utf-8').read()
    if path.endswith('.json'): return json.loads(t)
    i=t.index('const DATA = ')+len('const DATA = ')
    return json.JSONDecoder().raw_decode(t[i:])[0]

d=load(sys.argv[1])
print('anchor fit',d['anchor'].get('fit'),'| phi ast',d['calib']['phi']['ast|Stable'],d['calib']['phi']['ast|Volatile'])
def nb_over(mu,line,phi):
    if mu<=0: return 0
    r=mu/(phi-1);p=r/(r+mu);q=p**r;cdf=q
    for k in range(1,int(line)+1):
        q=q*(k-1+r)/k*(1-p);cdf+=q
    return 1-cdf
pay=lambda o:(o/100 if o>0 else 100/-o)
be=lambda o:1/(1+pay(o))
phi=d['calib']['phi']['ast|Stable']
G=lambda x:x.get('result') and x['result']['outcome'] in('W','L')
ea=[x for x in d['paper'] if x.get('early') and x['stat']=='ast' and x['date']<d['date']]
for x in ea:
    po=nb_over(x['proj'],x['line'],phi); pw=po if x['side']=='Over' else 1-po
    x['rawP']=pw; x['rawEV']=pw*pay(float(x['odds']))-(1-pw); x['rawEdge']=pw-be(float(x['odds']))
    x['cush']=abs(x['proj']-x['line']); x['pi']=float(x['odds'])<=-150
by=defaultdict(list)
for x in ea: by[x['date']].append(x)
def top3(l,key,skip_pi=False,pi_last=False):
    l=[x for x in l if not (skip_pi and x['pi'])]
    l=sorted(l,key=lambda x:((x['pi'] if pi_last else 0),key(x)))
    out=[]
    for x in l:
        if all(y['gameId']!=x['gameId'] for y in out): out.append(x)
        if len(out)==3: break
    return out
def score(picks):
    g=[x for x in picks if G(x)]; w=sum(x['result']['outcome']=='W' for x in g); u=sum(x['result']['flat'] for x in g)
    v=len([x for x in picks if not G(x)])
    lines=defaultdict(int)
    for x in g: lines['1.5' if x['line']<2 else '2.5-3.5' if x['line']<4 else '4.5+']+=1
    return w,len(g)-w,u,(u/len(g) if g else 0),v,dict(lines)
rules=[
 ('NOW: gap %, priced-in last', lambda x:-abs(x['gap']), dict(pi_last=True)),
 ('Card EV (anchored), priced-in last', lambda x:-x['ev'], dict(pi_last=True)),
 ('Card edge vs break-even, priced-in last', lambda x:-x['edge'], dict(pi_last=True)),
 ('Plain-projection EV, priced-in last', lambda x:-x['rawEV'], dict(pi_last=True)),
 ('Plain-projection EV, no filter', lambda x:-x['rawEV'], {}),
 ('Plain-projection hit chance, priced-in last', lambda x:-x['rawP'], dict(pi_last=True)),
 ('Assist cushion (proj - line), priced-in last', lambda x:-x['cush'], dict(pi_last=True)),
]
dates=sorted(by)
m=len(dates)//2
halves=[('first half',dates[:m]),('second half',dates[m:])]
print('halves:',dates[0],'-',dates[m-1],'|',dates[m],'-',dates[-1])
print(f"\n{len(dates)} nights, {len(ea)} Early assist plays ({sum(map(G,ea))} graded)\n")
for name,k,o in rules:
    allp=[x for t in dates for x in top3(by[t],k,**o)]
    w,l,u,roi,v,ln=score(allp)
    hs=[]
    for hn,ds in halves:
        hw,hl,hu,hr,_,_=score([x for t in ds for x in top3(by[t],k,**o)]); hs.append(f"{hw}-{hl} {hu:+.2f}u")
    print(f"{name:46} {w}-{l}  {u:+.2f}u  ROI {roi:+.0%}  | {hs[0]:>14} | {hs[1]:>14} | lines {ln}")
for name,f in [('ALL Early assists, flat 1u',lambda x:True),('Early assists not priced in',lambda x:not x['pi']),('Early assists priced in (-150 or shorter)',lambda x:x['pi'])]:
    p=[x for x in ea if f(x)]; w,l,u,roi,v,ln=score(p)
    hs=[]
    for hn,ds in halves:
        hw,hl,hu,hr,_,_=score([x for x in p if x['date'] in ds]); hs.append(f"{hw}-{hl} {hu:+.2f}u")
    print(f"{name:46} {w}-{l}  {u:+.2f}u  ROI {roi:+.0%}  | {hs[0]:>14} | {hs[1]:>14}")
# Not priced in, by line
print('\nNot priced in, by line bucket:')
B=defaultdict(list)
for x in ea:
    if not x['pi']: B[('1.5' if x['line']<2 else '2.5-3.5' if x['line']<4 else '4.5-6.5' if x['line']<7 else '7.5+')+' '+x['side']].append(x)
for k in sorted(B): w,l,u,roi,_,_=score(B[k]); print(f"  {k:14} {w}-{l} {u:+.2f}u ROI {roi:+.0%}")
# Rebounds by line, for the 4-6 question
print('\nRebounds by line (paper, graded, 1u flat):')
for lab,f in [('Best rebound look',lambda x:x.get('best') and x['stat']=='reb'),('Rebound Officials+Leans',lambda x:x['stat']=='reb' and not x.get('early') and not x.get('alt') and x.get('tier') in('Official','Lean'))]:
    R=defaultdict(list)
    for x in d['paper']:
        if f(x) and x['date']>='2026-11-01' and x['date']<d['date']:
            R['<=3.5' if x['line']<4 else '4.5-6.5' if x['line']<7 else '7.5+'].append(x)
    print(' ',lab, {k:'%d-%d %+.2fu'%score(v)[:3] for k,v in sorted(R.items())})
