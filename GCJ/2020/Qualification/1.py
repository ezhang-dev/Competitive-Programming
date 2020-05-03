def solve():
    n = int(input())
    q=[]
    for _ in range(n):
        q.append(list(map(int,input().split())))
    k = 0
    for i in range(n):
        k = k + q[i][i]
    r = 0
    for i in range(n):
        if len(set(q[i])) != n:
            r = r + 1
    qq = list(zip(*q))
    c = 0
    for i in range(n):
        if len(set(qq[i])) != n:
            c = c + 1
    return k ,r ,c
for z in range(int(input())):
    print("Case #"+str(z+1)+":",*solve())
