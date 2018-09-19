N=int(input())
data1=[]
i=0
while i<N:
    data1.append(list(map(lambda x:int(x),input().split(' '))))
    data1.sort()
    data2=[k[1] for k in data1]
    i+=1
print(data1[data2.index(max(data2))][0],max(data2))