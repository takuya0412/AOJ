n = int(input())
data = list(map(lambda x:int(x), input().strip().split(" ")))

def str_list(li):
    temp = list(map(lambda x:str(x),li))
    return " ".join(temp)


for i in range(1,n):
    print(str_list(data))
    j=i
    tgt = data[i]
    if tgt<data[j-1]:
        while tgt<data[j-1] and j>0:
            data[j] = data[j-1]
            j-=1
        data[j]=tgt
print(str_list(data))
