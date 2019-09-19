while True:
    n=input()
    if n=="0":break
    N=int(n)
    rec=[0]*N
    temp=""
    for i in range(N):
        temp=list(input().split(' '))
        rec[i]=[temp[0],temp.count("0")+temp.count("1")*-1]
    for i in range(N):
        for j in range(N-i-1):
            if rec[j][1]>=rec[j+1][1]:
                temp=rec[j]
                rec[j]=rec[j+1]
                rec[j+1]=temp
    for i in rec[::-1][0]:
        print(i)