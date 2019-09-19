while True:
    W=int(input())
    if W==0:break
    w=int(W/100)
    w2=int(w//2)
    ans=74848
    for i in range(w2+1):
        for j in range(int((w-i*2)//3)+1):
            for k in range(int((w-i*2-j*3)//5)+1):
                if i*2+j*3+k*5!=w:continue
                temp=(i//5*1520)+(i%5*380)+(j//4*1870)+(j%4*550)+(k//3*2244)+(k%3*850)
                if ans>temp:
                    ans=temp
    print(ans)