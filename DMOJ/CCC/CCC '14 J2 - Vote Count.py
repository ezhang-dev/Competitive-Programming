from collections import Counter
c=Counter()
input()
c.update(raw_input())
if c['A']>c['B']:
    print 'A'
if c['A']<c['B']:
    print 'B'
if c['A']==c['B']:
    print 'Tie'