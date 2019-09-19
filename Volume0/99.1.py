N,Q=list(map(lambda x:int(x),input().split(' ')))
data=[0]*N
data2=[]
i=0
while i<Q:
    data2.append(list(map(lambda x:int(x),input().split(' '))))
    i+=1
for num in data2:
    data[num[0]-1]=data[num[0]-1]+num[1]
    print(data.index(max(data))+1,max(data))

