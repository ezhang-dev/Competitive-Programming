def ip(x):
    if x<2:
        return False
    if x==2:
        return True   
    for y in xrange(2,int(x**0.5)+2):
        if (x%y==0):
            return False
    return True
q=input()
while not ip(q):
    q+=1
print q