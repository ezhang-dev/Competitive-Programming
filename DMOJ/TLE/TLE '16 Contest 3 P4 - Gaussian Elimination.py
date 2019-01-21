r=int(input())
c=int(input())
print(["First","Second"][(r+c)%2==0 and ((r!=1) and (c!=1))])