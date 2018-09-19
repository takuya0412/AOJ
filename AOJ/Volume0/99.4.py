N,Q=list(map(lambda x:int(x),input().split(' ')))
data=[0]*(N+1)

i=0
max_v=""
while i<Q:
    a,v=list(map(lambda x:int(x),input().split(' ')))
    data[a]=data[a]+v
    #print(f"a:{a},v{v}")
    #print(data)
    if i==0:
        #print("if")
        max_a=data.index(max(data))
        max_v=max(data)
    elif max_a==a:
        #print("elif1")
        if v<0:
            #print("elif1-if1")
            max_a=data.index(max(data))
            max_v=max(data)
        elif v>=0:
            max_v=data[a]

    elif max_a!=a:
        #print("elif2")
        if max_v==data[a]:
            #print("elif3-if1")
            if max_a>a:
                #print("elif3-if1-if1")
                max_a=a
        elif max_v<data[a]:
            max_a=a
            max_v=data[a]
    print(max_a,max_v)
    i+=1

