from math import cos,sin
def scal(vec,s):
    return [s*vec[0],s*vec[1],s*vec[2]]
def cross(a,b):
    return [a[1]*b[2]-b[1]*a[2],a[2]*b[0]-b[2]*a[0],a[0]*b[1]-b[0]*a[1]]
def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
def add(a,b):
    return [a[0]+b[0],a[1]+b[1],a[2]+b[2]]
def unit(vec):
    return scal(vec,1/dot(vec,vec)**0.5)
def rot(v,r,t):
    r=unit(r)
    return add(add(scal(v,cos(t)),scal(cross(r,v),sin(t))),scal(r,dot(v,r)*(1-cos(t))))
for _ in range(int(input())):
    i=list(map(float,input().split()))
    print("%.6f %.6f %.6f"%tuple(rot(i[0:3],i[3:6],i[6])))