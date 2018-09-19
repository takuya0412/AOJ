years=[num if (num%4==0 or num%400==0) and num%100!=0 else 0 for  num in range(1,3000)]
datasets=[]
n=0
while n<50:
    data=list(map(lambda x:int(x),input().split(' ')))
    if sum(data)==0:
        break
    n+=1
    ans=[res for res in years[data[0]:data[1]+1] if res!=0]
    if ans==[]:
        print("NA")
    else:
        for k in ans:
            print(k)
    print()