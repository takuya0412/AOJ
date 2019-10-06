N = int(input())
data = list(map(lambda x:int(x),input().strip().split(' ')))
cnt = 0
for i in range(N):
    min_n = i
    for j in range(i,N):
        if data[j] < data[min_n]:
            min_n = j
    if i != min_n:
        temp = data[i]
        data[i] = data[min_n]
        data[min_n] = temp
        cnt += 1
res = list(map(lambda x:str(x),data))
print(" ".join(res))
print(cnt)
