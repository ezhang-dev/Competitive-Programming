q=input()
s=[]
for _ in xrange(q):
    s.append(input())
s.sort()
if len(s)%2==1:
    print s[len(s)/2]
else:
    r=(s[len(s)/2-1]+s[len(s)/2])/2.
    print int(round(r))