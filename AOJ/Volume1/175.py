while True:
    ans=[]
    num=int(input())
    if num==-1:
        break
    while True:
        if num<4:
            ans.insert(0,num)
            print("".join([str(i) for i in ans]))
            break
        ans.insert(0,num%4)
        num//=4