def cup(change):
    num=len(change)-1
    #print(num)
    a=1
    b=c=0
    temp=0
    ans="A"
    for j in range(num):
        if change[j][0]!="A" and change[j][1]!="A":
            temp=b
            b=c
            c=temp
        elif change[j][0]!="B" and change[j][1]!="B":
            temp=a
            a=c
            c=temp
        elif change[j][0]!="C" and change[j][1]!="C":
            temp=a
            a=b
            b=temp
    if a==1:
        ans="A"
    elif b==1:
        ans="B"
    else:
        ans="C"
    return ans
i=0
change=[]
while i<50:
    try:
        #print("t1")
        change.append(input().strip().split(','))
        #print("change",change)
        if change[i][0]=="":
            break
    except EOFError:
        #print("error")
        break
    except IndexError:
        #print("error")
        break
    except ValueError:
        #print("error")
        break
    i+=1
print(cup(change))
