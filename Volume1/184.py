import math
while True:
    N=input()
    if N=="0":
        break
    num=[0]*7
    for i in range(int(N)):
        j=int(int(input())//10)
        if j>6:
            j=6
        num[j]+=1
    for i in num:
        print(i)