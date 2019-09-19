def calc(data):
    d=data
    leng=len(d)
    p_index=[num for num in range(leng) if data[num]=="peach"]
    a_index=[num for num in range(leng) if data[num]=="apple"]
    ##print(p_index)
    ##print(a_index)
    for j in range(len(p_index)):
        d[p_index[j]]="apple"
    for j in range(len(a_index)):
        d[a_index[j]]="peach"
        ##print(d)
    return d


sentence=input()
splitdata=[]
x=""
for k in sentence:
    ##print("x,k",x,k)
    ##print("k",k)
    if len(x)==0:
        #print("if")
        x+=k
    elif k.isalpha() and x[-1].isalpha():
        #print("elif1")
        x+=k
        ##print("x",x)
    elif k.isnumeric() and x[-1].isnumeric():
        #print("elif2")
        x+=k
    else:
        #print("else")
        ##print("x",x)
        splitdata.append(x)
        x=""
        x+=k
        


    print(splitdata)

print("last",splitdata)
print("".join(calc(splitdata)))