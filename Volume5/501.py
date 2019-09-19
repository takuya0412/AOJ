while True:
    n1=int(input().strip())
    if n1==0:break
    bfr=["0"]*n1
    aft=["0"]*n1
    for i in range(n1):
        bfr[i],aft[i]=map(str,input().strip().split(' '))
    n2=int(input().strip())
    data=[input().strip() for i in range(n2)]
    conv=[aft[bfr.index(i)] if i in bfr else i for i in data ]
    print("".join(conv))