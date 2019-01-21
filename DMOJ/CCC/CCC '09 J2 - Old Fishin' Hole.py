a=int(input())
b=int(input())
c=int(input())
t=int(input())
i=0

for x in range(t//a+1):
    for y in range(t//b+1):
        for z in range(t//c+1):
            if (x*a+y*b+z*c)<=t and x+y+z!=0:
                print("%d Brown Trout, %d Northern Pike, %d Yellow Pickerel"%(x,y,z))
                i+=1
print("Number of ways to catch fish: "+str(i))