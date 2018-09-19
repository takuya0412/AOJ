N=int(input())
i=0
while i<N:
    base=[0,0,0,0]
    outcnt=0
    point=0
    k=0
    while k<100:
        event=input()
        if event=="HIT":
            for d in range(1,4)[::-1]:
                base[d]=base[d-1]
                if base[3]==1:
                    point+=1
                    base[3]=0
            base[0]=1
            
        elif event=="HOMERUN":
            point+=sum(base)+1
            base=[0,0,0,0]
        
        elif event=="OUT":
            outcnt+=1
            if outcnt==3:
                print(point)
                break
        print("----event:",k,event)
        print("得点",point)
        print("出塁",base)
        print("アウト",outcnt)
        
        k+=1
    i+=1 