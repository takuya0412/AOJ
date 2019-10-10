N = int(input().strip())
S = list(map(lambda x:int(x),input().strip().split(' ')))
q = int(input().strip())
T = list(map(lambda x:int(x),input().strip().split(' ')))

def bin_search(N, i, S):
    cnt = 0
    min_i = 0
    max_i = N-1
    while True:
        middle_i = (min_i + max_i)//2
        if (max_i - min_i) == 0:
            if S[middle_i]==i:
                cnt = 1
            return cnt

        if S[middle_i] > i:
            max_i = middle_i
        elif S[middle_i] < i:
            min_i = middle_i+1
        else:
            cnt = 1
            return cnt

cnt = 0
for i in T:
    cnt += bin_search(N, i, S)
print(cnt)
