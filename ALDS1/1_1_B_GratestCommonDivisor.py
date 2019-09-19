data = list(map(lambda x:int(x), input().strip().split(" ")))
data.sort()
surplus = data[1]%data[0]
while surplus!=0:
    data[1] = surplus
    data.sort()
    surplus = data[1]%data[0]
print(data[0])
