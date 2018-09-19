import math
while True:
    cheese=list(map(lambda x:int(x),input().split(' ')))
    if cheese[0]==0:
        break
    N=int(input())
    cheese.sort()
    size=round(math.sqrt(cheese[0]**2+cheese[1]**2),1)
    i=0
    while i<N:
        data=int(input())
        if data*2>size:
            print("OK")
        else:
            print("NA")
        i+=1