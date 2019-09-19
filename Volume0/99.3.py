N,Q=list(map(lambda x:int(x),input().split(' ')))
data=[0]*(N+1)
i=0
max_v=""
while i<Q:
    a,v=list(map(lambda x:int(x),input().split(' ')))
    data[a]=data[a]+v
    if i==0:
        max_a=data.index(max(data))
        max_v=max(data)
    elif max_a==a:
        if v<0:
            max_a=data.index(max(data))
            max_v=max(data)
        elif v>=0:
            max_v=data[a]

    elif max_a!=a:
        if max_v==data[a]:
            if max_a>a:
                max_a=a
        elif max_v<data[a]:
            max_a=a
            max_v=data[a]
    print(max_a,max_v)
    i+=1

