def calc1(data1):
    count_dict=collections.Counter(data1)
    k,v=count_dict.most_common()[0]
    return k

def calc2(data2):
    leng=len(data2)
    max_str=len(data2[0])
    for i in range(1,leng):
        if max_str<len(data2[i]):
            max_str=len(data2[i])
            result=data2[i]
    return result


import collections
sentence=input().strip().split(' ')
print(f"{calc1(sentence)} {calc2(sentence)}")
