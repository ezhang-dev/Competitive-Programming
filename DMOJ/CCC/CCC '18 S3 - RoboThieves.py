import collections
mp=[]
y,x = map(int,input().split())
for _ in range(y):
    mp.append(list(input()))
sx=sy=-1
for a in range(y):
    for b in range(x):
        if mp[a][b]=='S':
            sx=b
            sy=a
            mp[a][b]='.'
for a in range(y):
    for b in range(x):
        if mp[a][b]=='C':
            mp[a][b]='W'
            for _ in range(a+1,y):
                if mp[_][b]=='W':
                    break
                if mp[_][b]!='.':
                    continue                
                mp[_][b]='X'
            for _ in range(a-1,-1,-1):
                if mp[_][b]=='W':
                    break
                if mp[_][b]!='.':
                    continue                 
                mp[_][b]='X'
            for _ in range(b+1,x):
                if mp[a][_]=='W':
                    break
                if mp[a][_]!='.':
                    continue                 
                mp[a][_]='X'
            for _ in range(b-1,-1,-1):
                if mp[a][_]=='W':
                    break
                if mp[a][_]!='.':
                    continue                 
                mp[a][_]='X'
#(x,y,d)
nex=collections.deque()
nex.appendleft((sx,sy,0))
while len(nex)!=0:
    x,y,d=nex.pop()
    if(mp[y][x]=='W' or mp[y][x]=='X'):
        continue
    #if(type(mp[y][x])==type(1)):
    #    mp[y][x]=min(d,mp[y][x])    
    if(mp[y][x]=='.'):
        mp[y][x]=d
        nex.appendleft((x,y-1,d+1))
        nex.appendleft((x-1,y,d+1)) 
        nex.appendleft((x,y+1,d+1))
        nex.appendleft((x+1,y,d+1))
    if(mp[y][x]=='S'):
        nex.appendleft((x,y-1,d+1))
        nex.appendleft((x-1,y,d+1)) 
        nex.appendleft((x,y+1,d+1))
        nex.appendleft((x+1,y,d+1))          
    if(mp[y][x]=='U'):
        nex.append((x,y-1,d))
        mp[y][x]='Q'
    if(mp[y][x]=='L'):
        nex.append((x-1,y,d))  
        mp[y][x]='Q'
    if(mp[y][x]=='D'):
        nex.append((x,y+1,d))  
        mp[y][x]='Q'
    if(mp[y][x]=='R'):
        nex.append((x+1,y,d))
        mp[y][x]='Q'

#print('\n'.join(map(lambda x:''.join(map(str,x)),mp)))
mp[sy][sx]='S'
for a in mp:
    for b in a:
        if b=='.' or b=='X':
            print(-1)        
        if type(b)==type(1):
            print(b)