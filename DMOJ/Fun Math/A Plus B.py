import sys
input = sys.stdin.readline
r=int(input())
for a in range(r):
    c=list(map(int,input().split(" ")))
    print (str(c[0]+c[1]))