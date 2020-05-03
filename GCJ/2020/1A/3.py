def solve():
   x,y = map(int,input().split())
   grid = []
   for _ in range(x):
    grid.append(list(map(int,input().split())))
   skill = 0
   done = False
   newGrid = [[0]*y for _ in range(x)]
   while not done:
        done=True
        for _ in range(x):
            skill = skill + sum(filter(lambda x:x!=-1, grid[_]))
        for i in range(x):
            for j in range(y):
                if grid[i][j] == -1:
                    newGrid[i][j] = -1
                    continue
                s = 0
                v = 0
                for q in range(i,-1,-1):
                    if grid[q][j] != -1:
                        s=s+grid[q][j]
                        v=v+1
                for q in range(j,-1,-1):
                    if grid[i][q] != -1:
                        s=s+grid[i][q]
                        v=v+1
                for q in range(i,x):
                    if grid[q][j] != -1:
                        s=s+grid[q][j]
                        v=v+1
                for q in range(j,y):
                    if grid[i][q] != -1:
                        s=s+grid[i][q]
                        v=v+1
                if grid[i][j]*v < s:
                    newGrid[i][j] = -1
                    done=False
                else:
                    newGrid[i][j] = grid[i][j]
        grid=newGrid
        newGrid = [[0]*y for _ in range(x)]
   return skill
for z in range(int(input())):
    print("Case #"+str(z+1)+":",solve())
