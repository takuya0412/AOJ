pre=[0]*100000000
route=[0]*1000000
def collatz(cnt,n):
    print("cnt,n",cnt,n)
    
    global route
    #n=1で再帰終了
    if n==1:
    #同じ計算はしなくて済むようにpreリストへ計算回数を格納
        for i in route:
            if pre[i]==0:
                pre[i]=cnt
                cnt-=1
        route=[]
        res=0
    #メモ化のためにリストへ使用した値を格納
    route[cnt]=cnt
    #計算済みであれば値を再使用する
    if n in pre:
        cnt+=pre[n]
        res=collatz(cnt,1)
        
    elif n%2==0:
        cnt+=1
        res=collatz(cnt,n/2)

    
    else:
        cnt+=1
        res=collatz(cnt,n*3+1)
    return res

collatz(0,1000)
k=0
while k<50:
    data=data=input()
    if data=="0":
        break
    print(pre[int(data)])
    cnt=0