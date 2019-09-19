def calc(data):
    b_array=[]
    b_count=0
    r0=data[0]
    r1=data[1]
    b=2
    res=1
    for k in range(max(data)):
        if r0>=b and r1>=b:
            if r0%b==0 and r1%b==0:
                r0/=b
                r1/=b
                b_count+=1
            else:
                if b_count>0:
                    b_array.append(b**b_count)
                else:
                    b_array.append(0)
                b_count=0
                b+=1
        elif r0<b or r1<b:
            b_array.append(b**b_count)
            for j in range(len(b_array)):
                if b_array[j]!=0:
                    res*=b_array[j]
            ans1=res
            ans2=r0*r1*res
            break
    return list(map(int,[ans1,ans2]))

i=1
while i<50:

    try:
        data = list(map(lambda x:int(x),input().strip().split()))
        if data[0]=="":
            break
        ans_data=calc(data)
        print(f"{ans_data[0]} {ans_data[1]}")

    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
