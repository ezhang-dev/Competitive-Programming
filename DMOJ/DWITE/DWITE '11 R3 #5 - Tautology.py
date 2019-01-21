def test(): 
    code=input().replace('~',' not ').replace('^',' and ').replace('v',' or ')
    q= 'Y'
    for x in range(0,1024):
        a=x&1
        b=x&2
        c=x&4
        d=x&8
        e=x&16
        f=x&32
        g=x&64
        h=x&128
        i=x&256
        j=x&512
        if not eval(code):
            q='N'
    return q
for _ in range(5):
    print(test() + test() + test())