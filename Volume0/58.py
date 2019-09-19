def calc(data):
    vec_ab=[data[2]-data[0],data[3]-data[1]]
    vec_cd=[data[6]-data[4],data[7]-data[5]]
    ans = "NO"

    t1=round(vec_ab[0]*vec_cd[0],12)
    t2=round(-1*vec_ab[1]*vec_cd[1],12)
    if t1==t2:
        ans="YES"
    else:
        ans="NO"
    return ans


import math
i=0
while i<100:
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
