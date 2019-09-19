ic=[0,6,7,5,5,20,15,0]
price=[[0,300,500,600,700,1350,1650],
       [300,0,350,450,600,1150,1500],
       [500,350,0,250,400,1000,1350],
       [600,450,250,0,250,850,1300],
       [700,600,400,250,0,600,1150],
       [1350,1150,1000,850,600,0,500],
       [1650,1500,1350,1300,1150,500,0]] 
while True:
    data=input()
    if data=="0":
        break
    d=int(data)
    t1=int("".join(list(input().split(' '))))
    a=int(input())
    t2=int("".join(list(input().split(' '))))
    if d>a:
        dis=sum(ic[a:d])
        p=price[a-1][d-1]
    else:
        dis=sum(ic[d:a])
        p=price[d-1][a-1]
    if (1730<=t1<=1930 or 1730<=t2<=1930) and dis<=40:
        while True:
            if p-50<price[d-1][a-1]/2:
                break
            p-=50
    print(p)