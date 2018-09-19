while True:
    data=input()
    if data=="0":
        break
    idata=int(data)
    cnt=0
    while True:
        if idata==1:
            break
        if idata%2==0:
            idata/=2
        elif idata%2!=0:
            idata=idata*3+1
        cnt+=1
    print(cnt)