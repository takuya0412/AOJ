primelist=[True]*10001
primelist[0]=False
primelist[1]=False
for i in range(2,10001):
    if primelist[i]==False:
        continue
    else:
        for k in range(i,10001):
            if k*i<=10000:
                primelist[k*i]=False

def twin(data):
    primedata=primelist[:data+1]
    l=0
    h=0
    for cnt in range(-1,-1*data,-1):
        if primedata[cnt]==primedata[cnt-2]==True:
            h=data+(cnt+1)
            l=data+(cnt-1)
            break
    return l,h
n=0
while n<10000:
    data=input()
    if data=="0":
        break
    data=int(data)
    low,high=twin(data)
    print(low,high)
    
    
