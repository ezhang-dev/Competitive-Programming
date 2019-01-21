for _ in range(int(input())):
    n=int(input())
    q=0
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            q+=x
            q+=n/x
            q-=(x==n/x)*x
    q+=1
    print(str(n)+' is '+('a deficient'if n>q else ('an abundant' if n<q else 'a perfect'))+' number.')