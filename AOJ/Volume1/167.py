while True:
    N=input()
    if N=="0":
        break
    n=int(N)
    num=[0]*n
    for i in range(n):
        num[i]=int(input())
    cnt=0
    for i in range(n-1):
        for j in range(n-1-i):
            if num[j]>num[j+1]:
                temp=num[j+1]
                num[j+1]=num[j]
                num[j]=temp
                cnt+=1
    print(cnt)