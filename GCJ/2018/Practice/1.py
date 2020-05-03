for _ in range(int(input())):
    a,b=map(int,input().split())
    a=1
    input()
    while True:
        mid=a+(b-a)//2
        print(mid)
        i=input()
        if i=="CORRECT":
            break
        elif i=="TOO_SMALL":
            a,b=mid+1,b
        elif i=="TOO_BIG":
            a,b=a,mid-1
        elif i=="WRONG_ANSWER":
            import sys
            sys.exit(1)