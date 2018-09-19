def weight(data):
    w=data
    bi_data=[]
    w_data=[]
    while True:
        a=w%2
        bi_data.append(a)
        w//=2
        if w==0:
            break
    w_data=[str(pow(2,x)) for x in range(len(bi_data)) if bi_data[x]==1]
    return w_data
   
i=0
while i<50:
    try:
        data=int(input())
        if data=="":
            break
        print(" ".join(weight(data)))
        i+=1
    except EOFError:
        break
    except ValueError:
        break
    except IndexError:
        break
