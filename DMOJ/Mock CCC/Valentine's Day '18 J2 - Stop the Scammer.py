g=int(input())
x,y=map(int,input().split())
s=0
i=0
while s<g and x>0:
    s+=2*x
    x-=y
    i+=1
print(i if s>=g else 'RIP')