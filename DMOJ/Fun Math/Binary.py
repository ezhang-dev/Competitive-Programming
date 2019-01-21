for _ in range(int(input())):
    a=bin(int(input()))[2:]
    if len(a)%4!=0:
        a='0'*(4-len(a)%4)+a
    print(' '.join([a[i:i+4] for i in range(0,len(a),4)]))