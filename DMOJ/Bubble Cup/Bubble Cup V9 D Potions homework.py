import sys
i=sys.stdin.readline
a=[]
b=int(i())
c=0
for _ in range(b):
    a.append(int(i()))
a.sort()
for _ in range(b):
    c=(c+a[_]*a[b-_-1])%10007
print(c)