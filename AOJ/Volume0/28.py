def calc(data):
    count_dict=collections.Counter(data)
    k,v=count_dict.most_common()[0]
    result=[k1 for k1,v1  in dict(count_dict).items() if v1==v]
    result.sort()
    return result


import collections
i=0
data = []
while i<100:
    try:
        data.append(int(input()))
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
    len=len(ans)
    for j in range(len):
        print(ans[j])
