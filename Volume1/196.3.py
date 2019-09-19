while True:
    n=input()
    if n=="0":break
    N=int(n)
    rec=[0]*N
    temp=""
    for i in range(N):
        temp=list(input().split(' '))
        rec[i]=[temp[0],temp.count("0")+temp.count("1")*-1]
    rec.sort(key=lambda x:(x[1],x[2]))
    for i in rec[::-1][0]:
        print(i)