def solve():
    d = 0
    s = map(int,input())
    o = ""
    for i in s:
        if i == d:
            pass
        elif i > d:
            o = o + "("*(i-d)
            d=i
        else:
            o = o + ")"*(d-i)
            d=i
        o=o+str(i)
    o=o+")"*d
    return o
for z in range(int(input())):
    print("Case #"+str(z+1)+":",solve())
