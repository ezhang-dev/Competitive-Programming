def run():
    a,b=map(int,input().split())
    input()
    while True:
        c=(a+b)//2
        print(c)
        out=input()
        if out=="CORRECT":
            return
        elif out=="TOO_SMALL":
            a=c
        else:
            b=c




for _ in range(int(input())):
    run()