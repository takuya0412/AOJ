N = int(input().strip())
in_data = [0]*N
for i in range(N):
    in_data[i] = int(input().strip())
cnt = 0
def insertion_sort(g):
    global cnt
    global in_data
    for i in range(g,N):
        print("i:",i)
        print(in_data)
        v = in_data[i]
        j = i-g
        while j>=0 and in_data[j] > v:
            in_data[j+g] = in_data[j]
            j-=g
            cnt +=1
        in_data[j+g] = v

def shell_sort(m,G):
    for j in range(m-1):
        insertion_sort(j)
G=[1]
m = len(G)
shell_sort(m,G)

print(m)
print(*G)
print(cnt)
for i in in_data:
    print(i)
