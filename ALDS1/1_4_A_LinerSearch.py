N = int(input().strip())
S = list(map(lambda x:int(x),input().strip().split(' ')))
q = int(input().strip())
T = list(map(lambda x:int(x),input().strip().split(' ')))
cnt = 0
for i in T:
    if i in S:
        cnt += 1
print(cnt)
