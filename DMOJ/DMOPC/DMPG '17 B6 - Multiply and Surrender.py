import math
input()
print(math.floor(sum(map(lambda x: math.log2(int(x)),input().split())))+1)