from functools import lru_cache

club=[]

@lru_cache(maxsize=None)
def hit(rem):
    if rem==0:
        return 0
    if rem<0:
        return 9999
    global club
    return min([hit(rem-x) for x in club])+1

d=int(input())

for _ in range(int(input())):
    club.append(int(input()))

r=hit(d)

if r>5280:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in "+str(r)+" strokes.")