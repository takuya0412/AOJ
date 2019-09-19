while True:
    n=int(input())
    if n==0:break
    f1=5
    f2=[4,1,3]
    f3=2
    f4=6
    p=1
    for i in range(n):
        rot=input()
        if rot[0]=="N":
            temp=f2[1]
            f2[1]=f3
            f3=f4
            f4=f1
            f1=temp
        elif rot[0]=="S":
            temp=f2[1]
            f2[1]=f1
            f1=f4
            f4=f3
            f3=temp
        elif rot[0]=="E":
            temp=f2[1]
            f2[1]=f2[0]
            f2[0]=f4
            f4=f2[2]
            f2[2]=temp
        elif rot[0]=="W":
            temp=f2[1]
            f2[1]=f2[2]
            f2[2]=f4
            f4=f2[0]
            f2[0]=temp
        elif rot[0]=="L":
            temp=f2[0]
            f2[0]=f1
            f1=f2[2]
            f2[2]=f3
            f3=temp
        elif rot[0]=="R":
            temp=f2[0]
            f2[0]=f3
            f3=f2[2]
            f2[2]=f1
            f1=temp
        p+=f2[1]
    print(p)