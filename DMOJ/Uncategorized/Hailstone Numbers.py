i=int(input())
j=0
while i!=1:
    if i%2==0:
        i=i//2
    else:
        i=i*3+1
    j+=1
print(j)