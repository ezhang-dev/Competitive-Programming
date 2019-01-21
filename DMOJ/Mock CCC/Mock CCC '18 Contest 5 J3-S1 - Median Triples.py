import sys
input=sys.stdin.readline
N,X = map(int,input().split())
d=list(map(int,input().split()))
d.sort()
med=[loc for loc, val in enumerate(d) if val == X]
m=len(med)
q=0
for i in med:
    if(i==0 or i==N-1):
        continue
    q+=(i)*(N-i-1)
print (q)