array = list(map(int, input().strip().split(' ')))
array_data=[num for num in array if 0<=num<=10000 if isinstance(num,int)]
array_data.sort()
print(array_data[-1])
print(array_data[-2])
print(array_data[-3])
