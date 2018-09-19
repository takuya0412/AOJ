while True:
    N=int(input())
    if N==0:
        break
    data=[]
    uriage=[0]*N
    i=0
    while i<N:
        data.append(list(map(lambda x:int(x),input().split(' '))))
        i+=1
    ans=[]
    num=list(dict.fromkeys([j[0] for j in data]))
    #print(data)
    #print("-----------")
    #print(num)
    for k in range(N):
        uriage[num.index(data[k][0])]=uriage[num.index(data[k][0])]+data[k][1]*data[k][2]
    for x in range(N):
        if uriage[x]>=1000000:
            ans.append(num[x])
    #print(uriage)
    if ans==[]:
        print("NA")
    else:
        for p in ans:
            print(p)


