def drop(data,pap):
    #print(data)
    #for p in range(2,12):
        #print(pap[p][2:12])
    x=data[0]+2
    y=data[1]+2
    if data[2]==1:
        pap[x][y]+=1
        pap[x-1][y]+=1
        pap[x+1][y]+=1
        pap[x][y-1]+=1
        pap[x][y+1]+=1
        
    elif data[2]==2:
        for a1 in range(x-1,x+2):
            for a2 in range(y-1,y+2):
                pap[a1][a2]+=1
    
    elif data[2]==3:
        for a1 in range(x-1,x+2):
            for a2 in range(y-1,y+2):
                pap[a1][a2]+=1
        pap[x-2][y]+=1
        pap[x+2][y]+=1
        pap[x][y-2]+=1
        pap[x][y+2]+=1
    #print("after ink")
    #for p in range(2,12):
        #print(pap[p][2:12])
    return pap
    
def ipap(pap):
    m_ink=[]
    num0=0
    for d in range(2,12):
        li=pap[d][2:12]
        #print("結果計算",d)
        #print("li",li,type(li))
        count_dict=dict(collections.Counter(li))
        #print("count_dict",count_dict)
        num0+=count_dict[0]
        #print("num0",num0)
        m_ink+=list(count_dict.keys())
        #print("m_ink",m_ink)
    max_ink=sorted(m_ink,reverse=True)[0]
    #print("max_ink",max_ink)
    return num0,max_ink

import collections
i=0
ink=[]
while i<50:
    try:
        #print("t1")
        ink.append(list(map(lambda x:int(x),input().strip().split(','))))
        #print("ink",ink)
        if ink[i][0]=="":
            break
    except EOFError:
        #print("error")
        break
    except IndexError:
        #print("error")
        break
    except ValueError:
        #print("error")
        break
#print("長さ",len(ink),ink)
    
pap=[[0]*14 for l in range(14)]
for j in range(len(ink)):
    pap=drop(ink[j],pap)
result=ipap(pap)
print(result[0])
print(result[1])


