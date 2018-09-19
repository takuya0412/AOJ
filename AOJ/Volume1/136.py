import math
N=int(input())
i=0
cnt=[0]*6
while i<N:
    h=float(input())
    if h<165.0:
        cnt[0]+=1
    elif 165.0<=h<170.0:
        cnt[1]+=1
    elif 170.0<=h<175.0:
        cnt[2]+=1
    elif 175.0<=h<180.0:
        cnt[3]+=1
    elif 180.0<=h<185.0:
        cnt[4]+=1
    elif 185.0<=h:
        cnt[5]+=1
    i+=1
for j in range(6):
    print(f"{j+1}:",end="")
    print("*"*cnt[j])