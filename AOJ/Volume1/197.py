while True:
    a,b=input().split(' ')
    if a=="0" and b=="0":break
    x=int(a)
    y=int(b)
    if int(a)<int(b):
        x=int(b)
        y=int(a)
    step=0
    while y!=0:
        x%=y
        temp=x
        x=y
        y=temp
        step+=1
    print(x,step)