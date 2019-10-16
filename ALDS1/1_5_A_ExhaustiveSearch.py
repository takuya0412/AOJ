N = int(input())
A = list(map(lambda x:int(x),input().strip().split(' ')))
q = int(input())
m = list(map(lambda x:int(x),input().strip().split(' ')))
dp = [""]
def calc(tgt, i):
    if tgt == 0:
        return True
    if i > N-1:
        return False
    return calc(tgt-A[i], i+1) or calc(tgt, i+1)


for tgt in m:
    if calc(tgt,0):
        print("yes")
    else:
        print("no")
