def calc(data1,data2join):
    res="pre-meiji"
    wareki="heisei"
    if 18680908<=data2join<=19120729:
        wareki="meiji"+" "+str(int(data1[0]-1868+1))
        res=wareki+" "+str(data1[1])+" "+str(data1[2])
    elif 19120730<=data2join<=19261224:
        wareki="taisho"+" "+str(int(data1[0]-1912+1))
        res=wareki+" "+str(data1[1])+" "+str(data1[2])
    elif 19261225<=data2join<=19890107:
        wareki="showa"+" "+str(int(data1[0]-1926+1))
        res=wareki+" "+str(data1[1])+" "+str(data1[2])
    elif 19890108<=data2join:
        wareki="heisei"+" "+str(int(data1[0]-1989+1))
        res=wareki+" "+str(data1[1])+" "+str(data1[2])
    else:
        res="pre-meiji"
    return res


N=0
while N<50:
    try:
        data1=list(map(lambda x:int(x),input().split(' ')))
        data2=[str(num) for num in data1]
        for i in range(1,3):
            if len(data2[i])==1:
                data2[i]="0"+data2[i]
        data2join=int("".join(data2))
    
        print(calc(data1,data2join))
        N+=1
    except ValueError:
        break
    except EOFError:
        break
    