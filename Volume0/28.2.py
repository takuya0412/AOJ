def calc(data):
    count_dict=collections.Counter(data)
    k,v=count_dict.most_common()[0]
    print()

    result=[k1 for k1,v1  in dict(count_dict).items() if v1==v]
    print(type(result))
    result.sort()
    print(result)
    return result


import collections
i=0
data = []
while i<100:
    try:
        data.append(int(input()))
        print(data,i)
        if data[i]==" ":
            break
        i+=1

    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
if len(data)>=1:
    ans=calc(data)
    print(ans)
    len=len(ans)
    for j in range(len):
        print(ans[j])
