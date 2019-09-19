def calc(data):
    count=0
    res=list(str(math.factorial(data)))
    for num in res[::-1]:
        if num!="0":
            break
        else:
            count+=1
    return count

import math
i=0
while i<20:
    try:
        data=int(input())
        if data==0:
            break
        print(calc(data))
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    i+=1

