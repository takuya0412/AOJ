N = int(input().strip())
S = list(map(lambda x:int(x),input().strip().split(' ')))
q = int(input().strip())
T = list(map(lambda x:int(x),input().strip().split(' ')))

# def bin_conpare(data,n,tgt):
#     n=-(-n//2)
#     print("n",n)
#     print("data\n",data)
#     if n == 1:
#         if data[0] == tgt:
#             return True
#         return False
#     if data[n]>tgt:
#         data=data[:n]
#         return bin_conpare(data, n, tgt)
#     elif data[n]<tgt:
#         data=data[n:]
#         return bin_conpare(data, n, tgt)
#     else:
#         return True
cnt = 0
for i in T:
    while N>0:
        N=-(-N//2)
        if N==1:
            if S[0]==i:
                cnt+=1
            break
        else:
            if S[N]>i:
                S=S[:N]
            elif S[N]<i:
                S=S[N+1:]
            else:
                cnt+=1
                break
print(cnt)
