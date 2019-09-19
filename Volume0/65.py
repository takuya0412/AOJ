def search(m1,m2):
    m1_min=sorted(list(set(m1)))
    res=[]
    for num1 in m1_min:
        if num1 in m2:
            temp1=[k for k in m1 if k==num1]
            temp2=[num2 for num2 in m2 if num2==num1]
            res.append([num1,len(temp1)+len(temp2)])
            temp1=[]
            temp2=[]
    return res

import collections
i=0
m1=[]
m2=[]
while i<1000:
    try:
        m1.append(list(map(lambda x:int(x),input().strip().split(',')))[0])
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
i=0
while i<1000:
    try:
        m2.append(list(map(lambda x:int(x),input().strip().split(',')))[0])
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break

res=search(m1,m2)
for ans in res:
    print(f"{ans[0]} {ans[1]}")
    




