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
    data=[input() for i in range(n2)]
    conv1=set([aft[bfr.index(i)] if i in bfr else i for i in data ])
    conv2=set([aft[bfr.index(i)] if i in bfr else i for i in data ])
    conv3=set([aft[bfr.index(i)] if i in bfr else i for i in data ])
    ans=list(conv1 | conv2 | conv3)
    if " " in ans:
        ans.remove(" ")
    print("".join(ans))