while True:
    n1=int(input())
    if n1==0:break
    bfr=["0"]*n1
    aft=["0"]*n1
    for i in range(n1):
        bfr[i],aft[i]=map(str,input().split(' '))
    print(bfr)
    print(aft)
    n2=int(input())
    conv=""
    for i in range(n2):
        temp=input()
        if temp in bfr:
            conv+=aft[bfr.index(temp)]
        else:
            conv+=temp
    print(conv)