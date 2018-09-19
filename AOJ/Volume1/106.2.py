nprice=[0]*51
se=[[15,2244],[10,1520],[12,1870],[5,850],[3,550],[2,380]]

for i in range(5,51):
    for j,p in se:
        temp=i
        sales=[0]*6
        cnt=0
        while temp>=j:
            temp-=j
            sales[cnt]+=p
        cnt=1
        if temp==1:
            continue
        if temp>=10:
            for k,p1 in se[cnt:3]:
                while temp>=k:
                    temp-=k
                    sales[cnt]+=p1
                cnt+=1
        
        if 0<temp<10:
            if temp%5==0:
                k,p1=se[3]

            elif temp%3==0:
                k,p1=se[4]
                    
            elif temp%2==0:
                k,p1=se[5]
                
            elif temp==7:
                sales[cnt]=1200
                temp=0
                
            while temp>=k:
                temp-=k
                sales[cnt]+=p1

        if temp!=0:
            continue
        price=sum(sales)
        
        if nprice[i]==0 or price<nprice[i]:
            nprice[i]=price

n=0         
while n<50:
    data=input()
    if data=="0":
        break
    ans=int(data)/100
    print(nprice[int(ans)])