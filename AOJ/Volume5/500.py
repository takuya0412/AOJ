while True:
    N=int(input())
    if N==0:break
    p1=0
    p2=0
    for i in range(N):
        a,b=map(int,input().split(' '))
        if a>b:p1+=a+b
        elif a<b:p2+=a+b
        else:
            p1+=a
            p2+=b
    print(p1,p2)