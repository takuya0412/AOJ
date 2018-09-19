def calc(data):
    vec_ab=[data[2]-data[0],data[3]-data[1]]
    vec_cd=[data[6]-data[4],data[7]-data[5]]
    ans = "NO"
    try:
        if vec_cd[0]==vec_ab[0]==0:
            ans="YES"
        else:
            t1=round(vec_ab[1]/vec_ab[0],6)
            t2=round(vec_cd[1]/vec_cd[0],6)
            if t1==t2:
                ans="YES"
            else:
                ans="NO"
    except ZeroDivisionError:
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
