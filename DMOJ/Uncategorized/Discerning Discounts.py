import sys
i=sys.stdin.readline
n,t=map(int,i().split())
t=t*100
q=0
for _ in range(n):
    c,d=map(int,i().split())
    if c*(100-d)<=t:
        q=q+1
print(q)