def solve():
    n = int(input())
    o = [""]*n
    c =0
    j =0
    z = []
    for i in range(n):
        a,b=map(int,input().split())
        z.append([a,b,i])
    z.sort(key=lambda x:x[0])
    for a,b,i in z:
        if a >= c:
            o[i]="C"
            c=b
        elif a >= j:
            o[i]="J"
            j=b
        else:
            return "IMPOSSIBLE"
    return "".join(o)

for z in range(int(input())):
    print("Case #"+str(z+1)+":",solve())
