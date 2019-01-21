tab=[]
s=int(input())
for _ in range(s):
    tab.append(list(map(int,input().split())))
while True:
    r=list(map(lambda x:x[0],tab))
    if(tab[0]==sorted(tab[0]) and r==sorted(r)):
        break
    nt=[None]*s
    for a in range(s):
        for b in range(s):
            if nt[b]==None:
                nt[b]=[]
            nt[b].append(tab[a][b])
    for r in nt:
        r.reverse()
            
    
    tab=nt
    
print('\n'.join(map(lambda x:' '.join(map(str,x)),tab)))