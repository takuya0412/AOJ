N,Q=list(map(lambda x:int(x),input().split(' ')))
data=[0]*N

i=0
while i<Q:
    a,v=list(map(lambda x:int(x),input().split(' ')))
    data[a-1]=data[a-1]+v
    print(data.index(max(data))+1,max(data))
    i+=1


