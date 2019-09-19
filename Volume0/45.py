def calc(data):
    dnum=len(data)
    mon=0
    num=0
    for j in range(dnum):
        num+=data[j][1]
        mon+=data[j][0]*data[j][1]
    res_num=Decimal(num/dnum).quantize(Decimal('0'),rounding=ROUND_HALF_UP)
    return mon,res_num
    
from decimal import Decimal,ROUND_HALF_UP
i=0
data=[]
while i<100:
    try:
        #print("t1")
        data.append(list(map(lambda x:int(x),input().strip().split(','))))
        #print("ink",ink)
        if data[i][0]=="":
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
result=calc(data)
print(result[0])
print(result[1])

    



