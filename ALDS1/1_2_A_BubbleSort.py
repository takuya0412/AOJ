N=int(input())
in_data = list(map(lambda x:int(x),input().strip().split(' ')))
flag = 1
cnt = 0
while flag:
    flag = 0
    for i in range(N-1, 0, -1):
        if in_data[i]<in_data[i-1]:
            temp = in_data[i]
            in_data[i] = in_data[i-1]
            in_data[i-1] = temp
            flag = 1
            cnt += 1

res = list(map(lambda x:str(x), in_data))
print(" ".join(res))
print(cnt)
