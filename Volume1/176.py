import math
colorlist=[[0,0,0],[0,0,255],[0,255,0],[0,255,255],
       [255,0,0],[255,0,255],[255,255,0],[255,255,255]]
while True:
    color=input()
    if color=="0":
        break
    R=int(color[1:3],16)
    G=int(color[3:5],16)
    B=int(color[5:],16)
    dmin=255
    num=0
    for  i in range(8):
        d=math.sqrt(abs(R-colorlist[i][0])**2+abs(G-colorlist[i][1])**2+abs(B-colorlist[i][2])**2)
        if dmin>d:
            dmin=d
            num=i
    if num==0:
        print("black")
    elif num==1:
        print("blue")
    elif num==2:
        print("lime")
    elif num==3:
        print("aqua")
    elif num==4:
        print("red")
    elif num==5:
        print("fuchsia")
    elif num==6:
        print("yellow")
    else:
        print("white")