while True:
    n=input()
    if n=="0":
        break
    N=int(n)
    data=[0]*N
    for i in range(N):
        data[i]=int(input())
    target=int(input())
    data.sort()
    cnt=1
    x=(N-1)//2
    if data[x]==target:
        print("*",cnt)
        continue
    while True:
        if len(data)==1:
            break
        x=(len(data)-1)//2
        cnt+=1
        print("x",x)
        if data[x]==target:
            break  
        if data[x]>target:
            data=data[:x]
        if data[x]<target:
            data=data[x+1:]
    print("*",cnt)
            