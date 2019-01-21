import sys
input=sys.stdin.readline
input()
d=list(map(int,input().split()))
l=len(d)
q=0
n=True
while n:
    n=False
    for i in range(l-1):
        if (d[i]<d[i+1]):
            n=True
            q+=1
            w=d[i]
            d[i]=d[i+1]
            d[i+1]=w
print (q)