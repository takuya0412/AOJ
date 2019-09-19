nprice=[0]*14
se=[[15,2244],[10,1520],[12,1870],[5,850],[2,380],[3,550]]

for i in range(5,14):
    print("**********i=",i)
    for j,p in se:
        print("***j,p",j,p)
        temp=i
        sales=[0]*6
        cnt=0
        while temp>=j:
            print("jwhileループtemp",temp)
            temp-=j
            sales[cnt]+=p
        cnt=1
        print("kループ突入時temp,sales",temp,sales)
        for k,p1 in se[cnt:]:
            while temp>=k:
                print("kwhileループtemp,k",temp,k)
                temp-=k
                sales[cnt]+=p1
            cnt+=1
            print(cnt,sales)
        if temp!=0:
            print("xxxxxxxxxxxx計算失敗xxxxxxxxxxxx",temp)
            continue
        price=sum(sales)
        print("price",price)
        print("nprice",i,nprice[i])
        if nprice[i]==0 or price<nprice[i]:
            print("値更新!")
            nprice[i]=price
        print("!After!nprice",i,nprice[i])
        

for n,num in enumerate(nprice[5:],5):
    print(n,num)
