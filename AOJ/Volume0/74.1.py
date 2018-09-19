def record(data):
    goukei_sec=0
    poss_record=[]
    for num in data:
        goukei_sec+=num[0]*3600+num[1]*60+num[2]
        #print("goukei_sec",goukei_sec)
    goukei_secx3=goukei_sec
    poss_record.append(7200-goukei_sec)
    poss_record.append(21600-goukei_secx3)
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
        h="0"+str(h)
        if m<10:
            m="0"+str(m)
        else:
            m=str(m)
            
        if s<10:
            s="0"+str(s)
        else:
            s=str(s)
        ans=h+":"+m+":"+s
        res.append(ans)
        #print("res",res)
    return res

import math
i=0
data=[]
while i<50:
    try:
        data.append(list(map(lambda x:int(x),input().strip().split(' '))))
        if data[i][0]==-1 and data[i][1]==-1 and data[i][2]==-1:
            data.pop()
            break
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    
ans=record(data)
#print("ans:",ans)
for j in ans:
    print(j)