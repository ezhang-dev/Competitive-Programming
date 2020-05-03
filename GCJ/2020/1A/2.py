def solve():
   n = int(input())
   i = 1
   while n > 0:
    print(str(i)+" 1")
    n=n-1
    if n >= i:
        print(str(i+1)+" 2")
        n=n-i
    i = i+1

for z in range(int(input())):
    print("Case #"+str(z+1)+":")
    solve()
