def calc(n):
    if n<=1:
        return 1
    else:
        if fib3[n]!=0:
            return fib3[n]
        elif n==2:
            fib3[n]=calc(n-1)+calc(n-2)
            return fib3[n]
        else:
            fib3[n]=calc(n-1)+calc(n-2)+calc(n-3)
            return fib3[n]
import math
while True:
    data=input()
    if data=="0":
        break
    N=int(data)
    fib3=[0]*(N+1)
    res=math.ceil(calc(N)/10)
    y=1
    y+=res//365
    print(y)
        
        