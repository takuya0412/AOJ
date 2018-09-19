while True:
    n=input()
    if n=="0":
        break
    N=int(n)
    data=[int(input()) for i in range(N)]
    target=int(input())
    data.sort()
    cnt=1
    x=(N-1)//2
    if data[x]==target:
        print("*",cnt)
        continue
    while True:
        print("x",x)
        print(data)
        print(data[x])
        x=(len(data)-1)//2
        if len(data)==1:
            break
        cnt+=1
        if data[x]==target:
            break  
        if data[x]>target:
            data=data[:x]
        if data[x]<target:
            data=data[x+1:]
        print("data",data)
        print(len(data))
    print("*",cnt)
            