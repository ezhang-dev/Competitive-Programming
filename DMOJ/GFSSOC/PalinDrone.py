m=10**9
n = int(input())
j = pow(10,n//2,m)
k = 2 * (j-1)
if n % 2 == 1:
  k=k+9*j
print(k%m)