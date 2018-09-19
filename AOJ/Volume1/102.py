while True:
    N=int(input())
    if N==0:
        break
    temp=[]
    matrix=[]
    ans=[]
    for i in range(N):
        matrix.append(list(map(lambda x:int(x),input().split(' '))))
    for j in range(N):
        cdata=[num[j] for num in matrix]
        temp.append(sum(cdata))
    matrix.append(temp)
    for k in range(len(matrix)):
        matrix[k].append(sum(matrix[k]))
        ans.append([str(num) for num in matrix[k]])
        print(" ".join(ans[k]))