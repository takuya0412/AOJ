def calc(data_a,data_b):
    a=set(data_a)
    b=set(data_b)
    hit=0
    res=list(a&b)
    res_len=len(res)
    for j in range(res_len):
        if data_a.index(res[j])==data_b.index(res[j]):
            hit+=1
    blow=res_len-hit
    return hit,blow



i=1
while i<=50:
    i+=1
    try:
        data_a = list(map(lambda x:float(x),input().strip().split()))
        if data_a[0]=="":
            break
        data_b = list(map(lambda x:float(x),input().strip().split()))
        result=calc(data_a,data_b)
        print(f"{result[0]} {result[1]}")
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
