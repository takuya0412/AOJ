N = int(input())
i_data = list(map(lambda x:int(x),input().strip().split(' ')))

def merge(left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = [i+left for i in range(n1)]
    R = [i+right for i in range(n2)]
    L[n1] = 10000000000
    L[n2] = 10000000000

    i = 0
    j = 0

    for k in range(left, right):
        if L[i] <= R[j]:


    
