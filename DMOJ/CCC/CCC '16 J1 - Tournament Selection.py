q=0
for _ in range(6):
   q+=raw_input()=='W' 
print 4-(q+1)/2 if q else -1