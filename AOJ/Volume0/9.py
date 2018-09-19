def calc(data):
    data=set([i for i in range(1,999999)])
    d2=set([i*2 for i in data if i*2<999999])
    d3=set([i*3 for i in data if i*3<999999])
    d5=set([i*5 for i in data if i*5<999999])
    d7=set([i*7 for i in data if i*7<999999])
    d11=set([i*11 for i in data if i*11<999999])
    d13=set([i*13 for i in data if i*13<999999])
    d17=set([i*17 for i in data if i*17<999999])
    data_min=list(data-d2-d3-d5-d7-d11-d13)
    p_number=0
    for k in data_min:
        count=0
        for j in range(2,k+1):
            if k%j==0:
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
