def calc(data):
    d=set([i for i in range(2,999999)])
    d2=set([i*2 for i in range(2,999999)])
    d3=set([i*3 for i in range(2,999999)])
    d5=set([i*5 for i in range(2,999999)])
    d7=set([i*7 for i in range(2,999999)])
    d11=set([i*11 for i in range(2,999999)])
    d13=set([i*13 for i in range(2,999999)])
    d17=set([i*17 for i in range(2,999999)])
    data_min=list(d-d2-d3-d5-d7-d11-d13-d17)
    data_min.sort()
    print(type(data_min),data_min[:20])
    p_number=0
    for k in data_min:
        print("---------k:",k)
        if data<k:
            break
        count=0
        for j in data_min:
            print("j:",j)
            if data<j:
                break
            elif k%j==0:
                print("カウントk,j:",k,j)
                count+=1
        if count==1:
            p_number+=1
    return (p_number)

i=1
while i<=30:
    try:
        data = int(input())
        if data=="":
            break
        print(calc(data))
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
