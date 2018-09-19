while True:
    n=input()
    if n=="0":
        break
    N=int(n)
    price=0
    cnt=0
    res=0
    record=[]
    while cnt<N:
        id,m1,s1,m2,s2,m3,s3,m4,s4=map(int,input().split(' '))
        time=(m1+m2+m3+m4)*60+s1+s2+s3+s4
        record.append([id,time])
        cnt+=1
    record.sort(key=lambda x:x[1])
    for i in range(2):
        print(record[i][0])
    print(record[-2][0])
