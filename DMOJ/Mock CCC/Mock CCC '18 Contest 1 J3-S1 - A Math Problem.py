k,p,x=map(int,input().split())
q=((k*p/x)**0.5)//1
f=lambda m:(m*x+k*p/m) if m!=0 else 99999999
print("%.3f"%(round(min(f(q),f(q+1)),3),))