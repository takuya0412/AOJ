import math
N=int(input())
res_money=100

for i in range(N):
    res_money=math.ceil(res_money*1.05)

print(res_money*1000)
