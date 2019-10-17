N = int(input())
A = list(map(lambda x: int(x), input().strip().split(' ')))
q = int(input())
m = list(map(lambda x: int(x), input().strip().split(' ')))
dp = [[""]]*(N+1)

def calc(tgt, i):
    if tgt == 0:
        return True
    if i > N-1:
        return False
    if A[i]>tgt:
        return calc(tgt, i+1)
    return calc(tgt-A[i], i+1) or calc(tgt, i+1)

def initialize():
    dp = [[""]]

for tgt in m:
    if calc(tgt,0):
        print("yes")
    else:
        print("no")
