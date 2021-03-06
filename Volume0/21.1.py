def calc(data):
    vec_ab=[data[0]-data[2],data[1]-data[3]]
    vec_cd=[data[4]-data[6],data[5]-data[7]]
    try:
        t1=round(vec_ab[0]/vec_cd[0],5)
        t2=round(vec_ab[1]/vec_cd[1],5)
        print(f"vec_ab:{vec_ab},vec_cd:{vec_cd},t1:{t1},t2:{t2}")
        if t1==t2:
            ans="YES"
        else:
            ans="NO"

    except ZeroDivisionError:
        if vec_cd[1]==vec_ab[1]==0:
            if vec_cd[0]==vec_ab[0]:
                ans="YES"
        else:
            ans="NO"
    return ans

import math
N=int(input())
i=1
while i<=N:
    i+=1
    try:
        data = list(map(lambda x:float(x),input().strip().split()))
        if data=="":
            break
        print(calc(data))
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
