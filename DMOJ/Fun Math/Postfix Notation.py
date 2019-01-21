s=[]
for t in input().split():
    if t=='*':
        s.append(s.pop()*s.pop())
    elif t=='/':
        s.append(s.pop(-2)/s.pop())
    elif t=='+':
        s.append(s.pop()+s.pop())
    elif t=='-':
        s.append(s.pop(-2)-s.pop())
    elif t=='%':
        s.append(s.pop(-2)%s.pop())
    elif t=='^':
        s.append(s.pop(-2)**s.pop())
    else:
        s.append(float(t))
print(s.pop())