def draw(n):
    for x in range(1,n+1,2):
        print('.'*((n-x)//2)+'#'*x+'.'*((n-x)//2))
    for x in range(n-2,0,-2):
        print('.'*((n-x)//2)+'#'*x+'.'*((n-x)//2))
for _ in range(5):
    draw(int(input()))