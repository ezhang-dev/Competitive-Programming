import re

stars = re.compile('\*+')

def solve():
    n = int(input())
    pad = ""
    start = ""
    end = ""
    fail = False
    for i in range(n):
        c = input().split("*")
        if c[0] != "":
            if len(start) >= len(c[0]):
                if not start.startswith(c[0]):
                    fail = True
            else:
                if c[0].startswith(start):
                    start=c[0]
                else:
                    fail = True
            c = c[1:]
        if c[-1] != "":
            if len(end) >= len(c[-1]):
                if not end.endswith(c[-1]):
                    fail = True
            else:
                if c[-1].endswith(end):
                    end=c[-1]
                else:
                    fail = True
            c = c[:-1]
        pad = pad + "".join(c)
    if fail:
        return "*"
    return start+pad+end

for z in range(int(input())):
    print("Case #"+str(z+1)+":",solve())
