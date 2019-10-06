N = int(input())
in_data = input().strip().split(" ")
split_data = [[i[0], int(i[1])] for i in in_data]

def babble_sort(data):
    flag = 1
    while flag:
        flag = 0
        for i in range(N-1, 0, -1):
            if data[i][1] < data[i-1][1]:
                temp = data[i]
                data[i]  = data[i-1]
                data[i-1] = temp
                flag = 1
    return data

def selection_sort(data):
    for i in range(N):
        min_i = i
        for j in range(i,N):
            if data[j][1]<data[min_i][1]:
                min_i = j
        temp = data[min_i]
        data[min_i] = data[i]
        data[i] = temp
    return data

def toTranp(data):
    return [el[0]+str(el[1]) for el in data]

def isStable(data):
    for i in range(1,10):
        tranp_data = toTranp(data)
        multi_data = [ el[0]+str(el[1]) for el in split_data if el[1]==i]
        if len(multi_data)>1:
            compare_list = [ el for el in tranp_data if el in multi_data]
            if compare_list == multi_data:
                continue
            else:
                return "Not stable"
        else:
            continue
    return "Stable"
babbled = babble_sort(split_data[:])
print(*toTranp(babbled))
print(isStable(babbled))
selected = selection_sort(split_data[:])
print(*toTranp(selected))
print(isStable(selected))
