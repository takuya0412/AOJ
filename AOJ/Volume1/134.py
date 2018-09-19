import math
N=int(input())
s=0
i=0
while i<N:
    s+=int(input())
    i+=1
print(math.floor(s/N))