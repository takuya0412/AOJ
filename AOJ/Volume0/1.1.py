array= [int(input()) for i in range(10)]
array_data=[num for num in array if 0<=num<=10000]
array_data.sort()
print(array_data[-1])
print(array_data[-2])
print(array_data[-3])
