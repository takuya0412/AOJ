i=1
while i<50:

    try:
        data = list(map(lambda x:int(x),input().strip().split()))
        if data[0]=="":
            break

        b_array=[]
        b_count=0
        r0=data[0]
        r1=data[1]
        b=2
        res=1
        for k in range(max(data)):
            if r0>=b and r1>=b:
                if r0%b==0 and r1%b==0:
                    print("if1")
                    r0/=b
                    r1/=b
                    b_count+=1
                    print(f"r0:{r0},r1:{r1}")
                    print(f"b_count:{b_count},b:{b}")
                else:
                    print("else1")
                    if b_count>0:
                        b_array.append(b**b_count)
                    else:
                        b_array.append(0)
                    print(b_array)
                    print(f"b_count:{b_count},b:{b}")
                    b_count=0
                    b+=1
            elif r0<b or r1<b:
                print("elif1")
                b_array.append(b**b_count)
                print("計算",b_array)
                print(f"計算b_count:{b_count},b:{b}")
                for j in range(len(b_array)):
                    if b_array[j]!=0:
                        res*=b_array[j]
                print(f"r0:{r0},r1:{r1},res:{res}")
                ans2=r0*r1*res
                break
        print("答えは",int(ans2))


    except EOFError:
        break
    except IndexError:
        break
