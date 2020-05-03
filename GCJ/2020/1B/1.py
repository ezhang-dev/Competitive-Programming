def bf(x):
    j = 1
    if x < 0:
        j = -1
        x = x * -1
    return [j if q =='1' else 0 for q in bin(x)[:1:-1]]

def m(r,i):
    if r[i] == r[i-1]:
        if i+1 == len(r):
            r.append(0)
        q= r[i]
        r[i-1] = -q
        r[i] = 0
        r[i+1] = r[i+1]+q
    elif r[i] == 0:
        q = r[i-1]
        r[i] = q
        r[i-1] = -q
    else:
        q = r[i]
        r[i] = -q
        r[i-1] = q

def solve():
    x,y = map(int,input().split())
    xArr = bf(x)
    yArr = bf(y)
    if abs(xArr[0]) == abs(yArr[0]):
        return "IMPOSSIBLE"
    i = 0
    while i < max(len(xArr),len(yArr)):
        if i == len(xArr):
            xArr.append(0)
        if i == len(yArr):
            yArr.append(0)
        if abs(xArr[i]) > 1:
            if i+1 == len(xArr):
                xArr.append(0)
            xArr[i+1] = xArr[i]//2+xArr[i+1]
            xArr[i] = xArr[i]%2
        if abs(yArr[i]) > 1:
            if i+1 == len(yArr):
                yArr.append(0)
            yArr[i+1] = yArr[i]//2+yArr[i+1]
            yArr[i] = yArr[i]%2 
        if abs(xArr[i]) == abs(yArr[i]):
            if xArr[i-1] != 0:
                m(xArr,i)
            else:
                m(yArr,i)
        i = i+1
    o = ""
    i = 0
    while i < len(xArr):
        if xArr[i] == 1:
            o = o +"E"
        elif xArr[i] == -1:
            o = o + "W"
        elif yArr[i] == 1:
            o = o + "N"
        else:
            o = o + "S"
        i = i + 1
    return o

for z in range(int(input())):
    print("Case #"+str(z+1)+":",solve())
