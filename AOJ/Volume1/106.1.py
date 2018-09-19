nprice=[0]*51
se=[[15,2244],[10,1520],[12,1870],[5,850],[3,550],[2,380]]

for i in range(5,51):
    #print("*******************i=",i)
    for j,p in se:
        #print("********割引j,p",j,p)
        temp=i
        sales=[0]*6
        cnt=0
        while temp>=j:
            #print("ループ1temp",temp)
            temp-=j
            sales[cnt]+=p
        #print("tempとsales",temp,sales)
        cnt=1
        if temp==1:
            continue
        if temp>=10:
            #print("temp10以上！！ループ2突入時temp,sales")
            #print(temp,sales)
            for k,p1 in se[cnt:3]:
                while temp>=k:
                    #print("whileループtemp,k",temp,k)
                    temp-=k
                    sales[cnt]+=p1
                cnt+=1
                #print("----sales",sales)
        
        if 0<temp<10:
            #print("temp10以下！！ループ2突入時temp,sales")
            #print(temp,sales)
            if temp%5==0:
                #print("route3")
                k,p1=se[3]

            elif temp%3==0:
                #print("route3")
                k,p1=se[4]
                    
            elif temp%2==0:
                #print("route2")
                k,p1=se[5]
                
            elif temp==7:
                #print("route7")
                sales[cnt]=1200
                temp=0
                
            while temp>=k:
                #print("whileループtemp,k",temp,k)
                temp-=k
                sales[cnt]+=p1

            #print("----cnt,sales",cnt,sales)
            
        if temp!=0:
            #print("xxxxxxxxxxxx計算失敗xxxxxxxxxxxx",temp)
            continue
        price=sum(sales)
        #print("price",price)
        #print("nprice",i,nprice[i])
        if nprice[i]==0 or price<nprice[i]:
            #print("値更新!")
            nprice[i]=price
        #print("!After!nprice",i,nprice[i])
        

for n,num in enumerate(nprice[5:],5):
    print(n,num)
