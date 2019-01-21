name=None
cit=[]
while name !="Waterloo":
    name,temp=input().split()
    cit.append((int(temp),name,))
t=min(cit,key=lambda x:x[0])
print(t[1])