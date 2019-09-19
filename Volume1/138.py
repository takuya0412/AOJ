temp=[0]*8
data=[0]*24
ans=[]
ans3=[0]*3
i=0
while i<24:
    data[i]=list(map(lambda x:float(x),input().split(' ')))
    i+=1
    cnt=0
for j,k in [(0,8),(8,16),(16,24)]:
    temp=sorted(data[j:k],key=lambda x:x[1])
    ans.append(temp[:2])
    ans3[cnt]=temp[2]
    temp=[0]*8
    cnt+=1
ans3.sort(key=lambda x:x[1])
ans.append(ans3[:2])
for x in range(4):
    for y in range(2):
        print(int(ans[x][y][0]),ans[x][y][1])
