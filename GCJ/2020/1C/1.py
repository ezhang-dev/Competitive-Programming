def solve():
    x,y,m = input().split()
    x = int(x)
    y = int(y)
    i = 0
    for z in m:
        i = i + 1
        if z == "N":
            y = y + 1
        elif z == "S":
            y = y -1
        elif z == "E":
            x = x +1
        else:
            x = x -1
        if abs(x) + abs(y) <= i:
            return i
    return "IMPOSSIBLE"

for z in range(int(input())):
    print("Case #"+str(z+1)+":",solve())
