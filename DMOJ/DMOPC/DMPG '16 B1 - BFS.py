c=(5,10,25,100,200)
d=map(int,input().split())
print(sum(map(lambda x:x[0]*x[1],zip(c,d))))