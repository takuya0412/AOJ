def calc(data):
    array=[]
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    n=i+j+k+l
                    if n==data:
                        array.append([i,j,k,l])

    return len(array)

i=1
while i<50:

    try:
        data = int(input())
        if data=="":
            break
        print(calc(data))

    except EOFError:
        break
    except ValueError:
        break
    except NameError:
        break
