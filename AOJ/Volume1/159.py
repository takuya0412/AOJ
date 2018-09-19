while True:
    N=input()
    if N=="0":
        break
    n=int(N)
    data=[0]*n
    for i in range(n):
        p,h,w=map(int,input().split(' '))
        data[p-1]=abs(22-w*10000/(h**2))
    print(data.index(min(data))+1)

        