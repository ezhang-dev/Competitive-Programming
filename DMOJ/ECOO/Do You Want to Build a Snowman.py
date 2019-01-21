head='''          |
       \  |  /
        \ | /
         \|/
       XXXXXXX
      X       X
     X  O   O  X
    X     V     X
W   X  X     X  X
 \   X  XXXXX  X
  \   X       X
   \   XXXXXXX
    \ X       X---
     X    O    X  \\
    X           X  \\
     XXXXXXXXXXX    \\'''.split("\n")
feet="""OOOO OOOO
OOOO OOOO""".split("\n")
def pad(f,x):
    return [' '*x+z for z in f]
def ll(x):
    if x==3:
        return 4
    return ll(x-1)+(x-1)-1
def pp(i,x):
    if i==x:
        return 0
    return pp(i+1,x)+i
def trap(x):
    dd=ll(x)
    lin=[]
    lin.append(' '*(x)+'X'+' '*(2*dd+1)+'X')
    for i in range(x-1):
        lin.append(' '*(x-i-1)+'X'+' '*(dd+i+1)+'O'+' '*(dd+i+1)+'X')
    lin.append('X'+' '*(2*dd+2*x+1)+'X')
    lin.append(' '+'X'*(2*dd+2*x+1))
    return lin
def snow(x):
    ss=pad(head,pp(2,x+1)-4)
    if x<=2:
        q=2
    else:
        q=0
    for i in range(3,x+2):
        ss+=pad(trap(i),max(q,pp(i,x+1)))
    if x<=2:
        ss+=pad(feet,6)
        if x==1:
            ss[16]+=" "
    else:
        ss+=pad(feet,(len(ss[-1])-7)//2)
    ss[16]+="     M"
    print('\n'.join(ss))
for _ in range(5):
    snow(int(input()))
    if _!= 4:
        print()