prime_list=[True]*1000000
prime_list[0]=False
prime_list[1]=False
for i in range(2,1000000):
    if prime_list[i]==False:
        continue
    elif prime_list[i]==True and i<1000:
        cnt=i
        while i*cnt<1000000:
            prime_list[i*cnt]=False
            cnt+=1

            

i=1
while i<=50:
    res=[]
    ans=0
    data = int(input())
    if data==0:
        break
    for k in range(2,1000000):
        if len(res)==data:
            ans=sum(res)
            break
        elif prime_list[k]==True:
            res.append(k)
    print(ans)
    i+=1
