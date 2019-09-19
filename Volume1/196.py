while True:
    n=input()
    if n=="0":break
    N=int(n)
    rec=[0]*N
    temp=""
    for i in range(N):
        temp=list(input().split(' '))
        print(temp)
        rec[i]=[temp[0],temp.count("0"),temp.count("1")]
    print(rec)
    for i in range(N-1):
        for j in range(N-i-1):
            if rec[j][1]>rec[j+1][1] or (rec[j][1]==rec[j+1][1] and rec[j][2]<=rec[j+1][2]):
                print("交換発生")
                print("比較対象",rec[j][1],rec[j+1][1])
                temp=rec[j]
                rec[j]=rec[j+1]
                rec[j+1]=temp
        print(rec)
    for ans in rec[::-1]:
        print(ans[0])