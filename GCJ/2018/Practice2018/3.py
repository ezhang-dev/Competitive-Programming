for cn in range(int(input())):
    d,n=map(int,input().split())
    t=[]
    for _ in range(n):
        k,s=map(int,input().split())
        t.append((d-k)/s)
    print("Case #%d: %.6f"%(cn+1,d/max(t)))