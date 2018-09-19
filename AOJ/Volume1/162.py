Hamming=[False]*1000001
Hamming[1]=True
for i in range(1,1000001):
    if i*2>1000000:
        break
    elif Hamming[i]==False:
        continue
    elif Hamming[i]==True:
        Hamming[i*2]=True
        if i*3<=1000000:
            Hamming[i*3]=True
        if i*5<=1000000:
            Hamming[i*5]=True
while True:
    data=input()
    if data=="0":
        break
    idata=list(map(int,data.split(" ")))
    print(Hamming[idata[0]:idata[1]+1].count(True))
