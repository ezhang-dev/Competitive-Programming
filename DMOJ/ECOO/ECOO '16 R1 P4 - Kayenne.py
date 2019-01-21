def dist(a,b,c,d):
    return (a-c)**2+(b-d)**2

def near(houses,x,y):
    n=t=0
    f=-1
    while n<3:
        dt=dn=0
        mm=80000
        for house in houses:
            d=dist(house[0],house[1],x,y)
            if d>mm or d<=f:
                continue
            if d<mm:
                dt=dn=0
                mm=d
            dt+=house[2]
            dn+=1
        n+=dn
        t+=dt
        f=mm
    return t<1
        
def run():
    houses=[]
    full=set()
    cx,cy=map(int,input().split())
    for i in range(100):
        x,y,d=input().split()
        houses.append((int(x),int(y),-1 if d=='D' else 1))
        full.add((int(x),int(y)))
    tot=0
    dem=0
    for x in range(cx-50,cx+51):
        for y in range(cy-50,cy+51):
            if dist(x,y,cx,cy)>2500 or (x,y) in full:
                continue
            tot+=1
            dem+=near(houses,x,y)
    print("%.1f"%(dem/tot*100,))
for _ in range(10):
    run()