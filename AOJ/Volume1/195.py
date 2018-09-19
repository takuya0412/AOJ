alpha=["A","B","C","D","E"]
while True:
    brk=0
    pos=0
    data=0
    for i in range(5):
        temp=sum(list(map(lambda x:int(x),input().split(' '))))
        if temp==0:
            brk=1
            break
        if data<temp:
            data=temp
            pos=i
    if brk==1:break
    print(alpha[pos],data)
    