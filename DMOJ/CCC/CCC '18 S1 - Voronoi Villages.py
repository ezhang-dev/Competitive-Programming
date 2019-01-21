n=[]
q=int(input())
for _ in range(q):
    n.append(int(input()))
n.sort()
m=10**10
for i in range(1,q-1):
    m=min(m,(-n[i-1]+n[i])/2+(-n[i]+n[i+1])/2)
print("%.1f"%(m,))