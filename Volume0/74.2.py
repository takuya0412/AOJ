def record(data):
    goukei_sec=0
    poss_record=[]
    goukei_sec+=data[0]*3600+data[1]*60+data[2]
        #print("goukei_sec",goukei_sec)
    goukei_secx3=goukei_sec
    poss_record.append(7200-goukei_sec)
    poss_record.append(poss_record[0]*3)
    #print(poss_record)

    res=[]
    for num in poss_record:
        h=0
        m=0
        s=num
        while s>=60:
            s-=60
            m+=1
            if m==60:
                m=0
                h+=1
        ho="0"+str(h)
        if m<10:
            mi="0"+str(m)
        else:
            mi=str(m)
            
        if s<10:
            se="0"+str(s)
        else:
            se=str(s)
        ans=ho+":"+mi+":"+se
        res.append(ans)
        #print("res",res)
    return res

import math
i=0

while i<50:
    try:
        data=list(map(lambda x:int(x),input().strip().split(' ')))
        if data[0]==-1 and data[1]==-1 and data[2]==-1:
            data.pop()
            break
        ans=record(data)
        #print("ans:",ans)
        for j in ans:
            print(j)
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    
