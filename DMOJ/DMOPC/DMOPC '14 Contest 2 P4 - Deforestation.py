import sys
i=sys.stdin.readline
s=[0]
q=0
for _ in range(int(i())):
    q+=int(i())
    s.append(q)
for _ in range(int(i())):
    a,b=map(int,i().split())
    print(s[b+1]-s[a])