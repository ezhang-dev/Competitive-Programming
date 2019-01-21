import sys
input=sys.stdin.readline
inf=(10**9)
rs=inf
re=-inf
ls=-inf
le=inf
p=[]
N,D=map(int,input().split())
for _ in range(N):
    p.append(int(input()))
for _ in range(D):
    s,e=map(int,input().split())
    if p[e-1]-p[s-1]>0:
        rs=min(rs,p[s-1])
        re=max(re,p[e-1])
    else:
        ls=max(ls,p[s-1])
        le=min(le,p[e-1])
rl=(re-rs) if rs!= inf else 0
ll=(-le+ls) if le!= inf else 0
s=min(abs(re-ls),abs(le-rs)) if (le!=inf and rs != inf) else 0
print(rl+ll+s)