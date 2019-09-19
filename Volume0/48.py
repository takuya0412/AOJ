def rank(data):
    ans=0
    if 40<=data<=48.00:
        ans="light fly"
    elif 48.00<data<=51.00:
        ans="fly"
    elif 51.00<data<=54.00:
        ans="bantam"
    elif 54.00<data<=57.00:
        ans="feather"
    elif 57.00<data<=60.00:
        ans="light"
    elif 60.00<data<=64.00:
        ans="light welter"
    elif 64.00<data<=69.00:
        ans="welter"
    elif 69.00<data<=75.00:
        ans="light middle"
    elif 75.00<data<=81.00:
        ans="middle"
    elif 81.00<data<=91.00:
        ans="light heavy"
    elif 91.00<data<=150.00:
        ans="heavy"
    return ans
i=0
while i<50:
    try:
        data=float(input())
        if data=="":
            break
        print(rank(data))
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    i+=1

