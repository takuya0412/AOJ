stop=[0,1,2,3,4,5,6,7,8,9,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9]
N=int(input())
i=0
while i<N:
    dest=list(map(lambda x:int(x),input().split(' ')))

    if dest[0]<=5 and dest[1]<dest[0]:
        ans=[num for num in range(dest[0],dest[1]-1,-1)]
    elif dest[1]>dest[0] or dest[0]>5:
        first=stop.index(dest[0])
        last=stop[first:].index(dest[1])+1+first
        ans=stop[first:last]
    print(" ".join([str(k) for k in ans]))
    i+=1