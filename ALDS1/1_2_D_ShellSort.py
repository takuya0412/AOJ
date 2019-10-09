N = int(input().strip())
in_data = [0]*N
for i in range(N):
    in_data[i] = int(input().strip())
cnt = 0

def create_shell_list(N):
    data = [1]
    for i in range(1,101):
        tmp = 3*data[0]+1
        if tmp>N or len(data)==100:
            break
        data.insert(0,tmp)
    return data

def insertion_sort(g):
    global cnt
    global in_data
    for i in range(g,N):
        v = in_data[i]
        j = i-g
        while j>=0 and in_data[j] > v:
            in_data[j+g] = in_data[j]
            j-=g
            cnt +=1
        in_data[j+g] = v

def shell_sort(G):
    for j in G:
        insertion_sort(j)
G=create_shell_list(N)
shell_sort(G)

print(len(G))
print(*G)
print(cnt)
for i in in_data:
    print(i)
