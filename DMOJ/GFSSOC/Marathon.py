import sys
i=sys.stdin.readline
s=[0]
q=0
x,y = input().split()
for _ in i().split():
    q+=int(_)
    s.append(q)

for _ in range(int(y)):
    a,b=map(int,i().split())
    print(q-s[b]+s[a-1])