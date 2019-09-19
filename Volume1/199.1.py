while True:
    n,m=input().split(' ')
    if n=="0":break
    N=int(n)
    M=int(m)
    chair=["#"]*(N+2)
    chair[0]=chair[N+1]="x"
    for i in range(M):
        sit=False
        p=input()
        if p=="A":
            for j in range(1,N+1):
                if chair[j]=="#":
                    chair[j]=p
                    break
        elif p=="B":
            pos=N-1
            for j in range(N+1,0,-1):
                if chair[j]=="#":
                    pos=j
                    if chair[j-1]!="A" and chair[j+1]!="A":
                        sit=True
                        chair[j]=p
                        break
            if sit==False:
                chair[pos]=p
        elif p=="C":
            if chair.count("#")==N:
                if N%2==0:
                    chair[N//2+1]=p
                else:
                    chair[(N+1)//2]=p
            else:
                for j in range(1,N+1):
                    if chair[j]!="#":
                        if chair[j+1]=="#":
                            chair[j+1]=p
                            break
                        elif chair[j-1]=="#":
                            chair[j-1]=p
                            break
        else:
            if chair.count("#")==N+2:
                chair[1]=p
            else:
                open_c=[0]*(N+2)
                for j in range(1,N+2):
                    cnt=[0]*2
                    r_flag=0
                    l_flag=0
                    for k in range(j+1,N+2):
                        if chair[k]!="#":
                            if chair[k]=="x":
                                r_flag=1
                            break
                        cnt[0]+=1
                    for k in range(j-1,-1,-1):
                        if chair[k]!="#":
                            if chair[k]=="x":
                                l_flag=1
                            break
                        cnt[1]+=1
                    if r_flag==1 and l_flag==1:
                        open_c[j]=max(cnt)
                    elif r_flag==1 and l_flag==0:
                        open_c[j]=cnt[1]
                    elif r_flag==0 and l_flag==1:
                        open_c[j]=cnt[0]
                    else:
                        open_c[j]=min(cnt)
                for s in range(N+2):
                    if chair[s]!="#":
                        open_c[s]=-1
                space=open_c.index(max(open_c))
                chair[space]=p
    print("".join(chair[1:N+1]))