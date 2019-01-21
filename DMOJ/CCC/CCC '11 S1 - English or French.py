from collections import Counter
c=Counter()
for _ in xrange(input()):
   c.update(raw_input())
print "French" if (c['s']+c['S'])>=(c['t']+c['T']) else "English"