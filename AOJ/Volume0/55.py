def calc(data):
    ans=[]
    ans.append(data)
    for j in range(10):
        if j%2==0:
            print("if")
            ans.append(ans[j]*2)
        else:
            print("else")
            ans.append(ans[j]/3)
    print(ans)
    return Decimal(sum(ans)).quantize(Decimal('0.000001'),rounding=ROUND_HALF_UP)

from decimal import Decimal,ROUND_HALF_UP
i=0
while i<50:
    try:
        data=float(input())
        if data=="":
            break
        print(calc(data))
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    i+=1

