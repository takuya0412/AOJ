collatzlist=[0]*10000000
cnt=1
i=2
while cnt<100:
    if i%2==0:
        i*=2
    else:
        i=(i-1)/3
    print(i)
    collatzlist[i]=cnt
    cnt+=1
print(collatzlist)
while i<50:
    data=input()
    if data=="0":
        break
    print(collatzlist[int(data)])
    