while True:
    n=input()
    if n=="0":
        break
    N=int(n)
    data=[int(input()) for i in range(N)]
    target=int(input())
    cnt=0
    lsb=0
    msb=len(data)-1
    while True:
        if msb<lsb:break
        else:
            x=lsb+(msb-lsb)//2
            cnt+=1
            if data[x]==target:break
            if msb==lsb:break
            if data[x]>target:
                msb=x-1
            elif data[x]<target:
                lsb=x+1
    print(cnt)