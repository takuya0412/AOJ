N,Q=list(map(lambda x:int(x),input().split(' ')))
data=[0]*N

i=0
while i<Q:
    a,v=list(map(lambda x:int(x),input().split(' ')))
    data[a-1]=data[a-1]+v
    data2=sorted(data,reverse=True)[0]
    print(data.index(data2)+1,data2)
    i+=1

