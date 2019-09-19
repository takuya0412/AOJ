def Gcalc(data):
    a=2
    for l in range(2,max(data)):
        if data[0]<a or data[1]<a:
            print("if1")
            ans1=1
            break
            if data[0]%a==0 and data[1]%a==0:
                print("if2")
                ans1=a
                break
        else:
            print("else")
            a+=1
    return ans1

def Lcalc(data):
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
            ans2=r0*r1*res
            break
    return int(ans2)

i=1
while i<50:

    try:
        data = list(map(lambda x:int(x),input().strip().split()))
        if data[0]=="":
            break
        print(f"{Gcalc(data)} {Lcalc(data)}")

    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
