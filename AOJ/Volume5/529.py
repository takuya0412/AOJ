while True:
    ans=[]
    N,M=map(int,input().split(' '))
    p=[0]*N
    m=[-1]*N
    if N==0 and M==0:
        break
    dp=[0]*(N+1)
    for i in range(N):
        p[i]=int(input())
    for i in range(N+1):
        dp[i]=[0]*5
        print(dp[i])
    
    for i in range(N):
        for j in range(5):
            if j<1:
                dp[i][j]
            else:
                a1=dp[i][j]
                a2=dp[i+1][j-1]+p[i]
                print(a1,a2,max(a1,a2))
                #if a2>M:
                 #a2=0
                dp[i+1][j]=max(a1,a2)
                if dp[i+1][j]>M:
                    dp[i+1][j]=0
    print("-"*20)
    for i in dp:
        ans.append(max(i))
        print(i)
        
    print("結果:",max(ans))