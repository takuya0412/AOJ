N=int(input())
data = [list(map(lambda x:int(x),input().strip().split())) for i in range(N)]

for i in range(N):
    data[i].sort(reverse=True)
    a=data[i][0]
    b=data[i][1]
    c=data[i][2]
    if a**2==b**2+c**2:
        print("YES")
    else:
        print("NO")
