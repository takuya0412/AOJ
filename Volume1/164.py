while True:
    N=32
    data=input()
    if data=="0":
        break
    n=int(data)
    ziro=list(map(lambda x:int(x),input().split(' ')))
    turn=0
    cnt=0
    while True:
        if N<=0:
            break
        turn+=1
        if turn%2!=0:
            N-=(N-1)%5
            print(N)
        elif turn%2==0:
            if cnt==n:
                cnt=0
            if ziro[cnt]>N:
                N=0
                print(N)
            else:
                N-=ziro[cnt]
                cnt+=1
                print(N)