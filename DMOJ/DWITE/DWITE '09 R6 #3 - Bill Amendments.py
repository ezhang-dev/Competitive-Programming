class bill():
    id=""
    amt=0
for _ in range(5):
    b=[]
    for __ in range(int(input())):
        bl=bill()
        bl.id,bl.amt=input().split()
        bl.amt=int(bl.amt)
        b.append(bl)
    for __ in range(int(input())):
        id,amt=input().split()
        amt=int(amt)
        for bl in b:
            if bl.id==id and bl.amt>0:
                d=min(amt,bl.amt)
                bl.amt-=d
                amt-=d
            if amt==0:
                break
    for bl in b:
        print(bl.id+" "+str(bl.amt))