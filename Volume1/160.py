while True:
    n=input()
    if n=="0":
        break
    N=int(n)
    price=0
    cnt=0
    res=0
    while cnt<N:
        x,y,h,w=map(int,input().split(' '))
        l=x+y+h
        if l<=60 or w<=2:
            price=600
        if 60<l<=80 or 2<w<=5:
            price=800
        if 80<l<=100 or 5<w<=10:
            price=1000
        if 100<l<=120 or 10<w<=15:
            price=1200
        if 120<l<=140 or 15<w<=20:
            price=1400
        if 140<l<=160 or 20<w<=25:
            price=1600
        if 160<l or 25<w:
            price=0
        res+=price
        cnt+=1
    print(res)