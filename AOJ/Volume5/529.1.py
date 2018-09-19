while True:
    ans=[]
    N,M=map(int,input().split(' '))
    p=[0]*N
    if N==0 and M==0:
        break
    dp=[0]*(N+1)
    for i in range(N):
        p[i]=int(input())
    for i in range(N+1):
        dp[i]=[0]*(M+1)
        print(dp[i])
    
    for i in range(N):
        cnt=0
        for j in range(min((M+1),p[i]*4+1)):
            if j<p[i]:
                dp[i+1][j]=dp[i][j]
            else:
                dp[i+1][j]=max(dp[i][j],dp[i+1][j-p[i]]+p[i])
                    
                

    print("-"*20)
    for i in dp:
        ans.append(max(i))
        print(i)
        
    print("結果:",max(ans))