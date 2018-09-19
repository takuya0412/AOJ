while True:
    n=input()
    if n=="0":
        break
    data=[int(input()) for i in range(int(n))]
    target=int(input())
    cnt=1
    i=(len(data)-1)//2
    while True:
        if len(data)==1:
            break
        i=(len(data)-1)//2
        cnt+=1
        if data[i]==target:
            break
        elif data[i]>target:
            data=data[:i]
        else:
            data=data[i+1:]
    print(cnt)
            