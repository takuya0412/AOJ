def calc(data):
    card=[num for num in range(1,11)if num!=data[0] if num!=data[1] if num!=data[2]]
    cards=0
    my=20-data[0]-data[1]
    for j in range(7):
        if card[j]>my:
            break
        cards=j+1
    return cards/7


import math
while True:
    try:
        data = list(map(lambda x:int(x),input().split(" ")))
        if data[0]=="":
            break
        ans=calc(data)
        if ans>=0.5:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    
