N, q = map(lambda x:int(x),input().strip().split(' '))
in_data = []
for i in range(N):
    a, b = input().strip().split(' ')
    in_data.append([a, int(b)])
res_data = []
cnt = 0
while len(in_data):
    tgt = in_data.pop(0)
    if tgt[1] <= q:
        total = cnt + tgt[1]
        res_data.append([tgt[0], total])
        cnt+=tgt[1]
    else:
        tgt[1] -= q
        in_data.append(tgt)
        cnt+=q

for j in res_data:
    print(*j)
