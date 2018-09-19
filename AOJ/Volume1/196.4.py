while True:
    n=input()
    if n=="0":break
    N=int(n)
    rec=[0]*N
    temp=""
    for i in range(N):
        temp=list(input().split(' '))
        rec[i]=[temp[0],temp.count("0"),temp.count("1")*-1,N-i]
    rec.sort(key=lambda x:(x[1],x[2],x[3]))
    for ans in rec[::-1]:
        print(ans[0])