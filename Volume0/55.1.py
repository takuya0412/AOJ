def calc(data):
    ans=0
    for j in range(1,11):
        if j%2==0:
            ans+=2*data*pow((2/3),j/2-1)
        else:
            ans+=data*pow((2/3),(j-1)/2)
    return round(ans,8)

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

