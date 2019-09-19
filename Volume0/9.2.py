def calc(data):
    d_list=[k for k in range(2,data+1)]
    d_set=set(d_list)
    p=2
    cnt=0
    while p<math.sqrt(data):
        print("d_list",d_list)
        p=d_list[cnt]
        print("p",p,"cnt",cnt)
        p_list=[j*p for j in range(p,round(data/p)+1)]
        print("p_list",p_list)
        p_set=set(p_list)
        print("d_set",d_set)
        print("p_set",p_set)
        d_list=list(d_set-p_set)
        d_list.sort()
        d_set=set(d_list)
        cnt+=1
    res=len(d_list)


    return res
    

import math
i=1
while i<=30:
    try:
        data = int(input())
        print(calc(data))
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
