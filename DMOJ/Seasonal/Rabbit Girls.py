import sys
input = sys.stdin.readline
r=int(input())
q=int(input())
if r < q:
    print (q-r)

else:
    e=r%q
    a=q-(r%q)

    print(str(min(e,a)))