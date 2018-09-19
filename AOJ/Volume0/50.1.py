
def calc(splitdata):
    d=splitdata
    leng=len(d)
    data=[num.lower() for num in splitdata] 
    temp=""
    string=""
    app="apple"
    pea="peach"
    p_index=[num for num in range(leng) if data[num]=="peach"]
    a_index=[num for num in range(leng) if data[num]=="apple"]
    #print(p_index)
    #print(a_index)
    for j in p_index:
        #print("------------j:",j)
        index=0
        temp=d[j]
        for k in temp:
            #print("k:",k)
            if k.islower():
                #print("app if")
                string+=app[index]
            else:
                #print("app else")
                string+=app[index].upper()
            #print("string",string)
            index+=1
        temp=""
        d[j]=string
        string=""
            

        
    for j in a_index:
        #print("------------j:",j)
        index=0
        temp=d[j]
        for k in temp:
            #print("k:",k)
            if k.islower():
                #print("pea if")
                string+=pea[index]
            else:
                #print("pea else")
                string+=pea[index].upper()
            #print("string",string)
            index+=1
        temp=""
        d[j]=string
        string=""
    return d


sentence=input()
splitdata=[]
count=0
x=""
for k in sentence:
    count+=1
    #print("x,k",x,k)
    #print("k",k)
    if len(x)==0:
        #print("if")
        x+=k
    elif x.lower()=="apple" or x.lower()=="peach":
        splitdata.append(x)
        x=""
        x+=k
        
    elif k.isalpha() and x[-1].isalpha():
        #print("elif1")
        x+=k

    elif k.isnumeric() and x[-1].isnumeric():
        #print("elif2")
        x+=k
    else:
        #print("else")
        #print("x",x)
        splitdata.append(x)
        x=""
        x+=k
        if count==len(sentence):
            #print("else-if")
            splitdata.append(x)
            x=""
    #print(splitdata)
if len(x)!=0:
    splitdata.append(x)

    
#print("last",splitdata)
print("".join(calc(splitdata)))
