def num(l):
    return [ord(x)-ord('A') for x in l]

def let(l):
    return [chr(x+ord('A')) for x in l]
c=num(input())
k=num(input())
p=[]
for (i,l) in enumerate(c):
    q=(l-k[i]+26)%26
    k.append(q)
    p.append(q)

print(''.join(let(p)))