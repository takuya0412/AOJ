array = [list(map(lambda x:int(x),input().strip().split())) for i in range(200)]
for i in range(0,200):
    count=1
    s=sum(array[i])
    while True:
        s/=10
        if s<1:
            break
        count+=1
    print(count)
