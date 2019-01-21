import datetime
a,b=map(int,input().split())
c,d=map(int,input().split())
t=abs(a-c)+abs(b-d)
d=datetime.datetime.strptime(input(),"%Y:%m:%d:%H:%M:%S")
d=d+datetime.timedelta(0,t)
print(d.strftime("%Y:%m:%d:%H:%M:%S"))