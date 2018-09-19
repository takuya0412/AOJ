while True:
    d=list(map(lambda x:int(x),input().split(' ')))
    if d[0]==0:
        break
    ans="NA"
    res=[i+(d[1]-i*d[2])//d[3] for i in range(0,d[4]+1)]
    for i in range(d[4],-1,-1):
        if res[i]>=d[0] and 0<i<=d[4] and res[i]-i>=0:
            ans=(i,res[i]-i)
            break
    if ans=="NA":
        print(ans)
    else:
        print(ans[0],ans[1])
        