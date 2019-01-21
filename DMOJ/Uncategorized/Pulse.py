n,s,t = map(int,input().split())
i=0
for _ in range(n):
    q=2*int(input())
    if s<=q and q<=t:
        i+=1
print(i)