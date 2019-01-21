c=[0,100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
i=int(input())
for _ in range(i):
    c[int(input())]=0
print('deal' if sum(c)/(10-i)<int(input()) else 'no deal')