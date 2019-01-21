q=input()
r=0
s=[]
for _ in xrange(q):
    s.append(raw_input())
for t in xrange(q):
    r+=(s[t]==raw_input())
print r