for _ in range(10):
    n=int(input())
    a=input().split()[::-1]
    b=[""]
    i=0
    while a:
        w=a.pop()
        if  len(b[i])+1+len(w)<=n:
            b[i]+=(" "if b[i] else '')+w
        else:
            if len(w)>n:
                a.append(w[n:])
                w=w[:n]
            i+=1
            b.append(w)
    print('\n'.join(b))
    print('='*5)