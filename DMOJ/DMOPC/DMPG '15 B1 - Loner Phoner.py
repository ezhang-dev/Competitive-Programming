for _ in range(int(input())):
    p=input()
    if len(p)==10 and (p[0:3]=='647' or p[0:3]=='416'):
        print('('+p[0:3]+')-'+p[3:6]+'-'+p[6:10])
    else:
        print ('not a phone number')