years=[num if num%4==0 else 0 for  num in range(1,3000)]
leap_years=[0 if (num%100==0 and num%400!=0) else num for num in years]
datasets=[]
n=0
while n<50:
    datasets.append(list(map(lambda x:int(x),input().split(' '))))
    if sum(datasets[n])==0:
        datasets.pop()
        break
    n+=1
cnt=0
for data in datasets:
    cnt+=1
    ans=[res for res in leap_years[data[0]-1:data[1]] if res!=0]
    if ans==[]:
        print("NA")
    else:
        for k in ans:
            print(k)
    if cnt==len(datasets):
        break
    print()