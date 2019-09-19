def calc(data):
    min_data=int("".join(sorted(data)))
    max_data=int("".join(sorted(data,reverse=True)))
    return max_data-min_data

N=int(input())
i=1

while i<=N:
    i+=1
    try:
        data = list(input())
        if data=="":
            break
        print(calc(data))
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
