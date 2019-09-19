def calc(data):
    d=data
    leng=len(d)
    p_index=[num for num in range(leng) if data[num]=="peach"]
    a_index=[num for num in range(leng) if data[num]=="apple"]
    print(p_index)
    print(a_index)
    for j in range(len(p_index)):
        d[p_index[j]]="apple"
    for j in range(len(a_index)):
        d[a_index[j]]="peach"
        print(d)
    return d


sentence=input()
splitdata=[]
x=""

for k in sentence:
    print("k",k)
    if k.isalpha():
        print("if1")
        x+=k
        print("x",x)
    else:
        print("else")
        print("x",x)
        splitdata.append(x)
        if k!=" ":
            splitdata.append(k)
        x=""

print(splitdata)
res=calc(splitdata)
ans=res[0]
for num in range(1,len(res)):

    if res[num].isalpha()==False and res[num].isnumeric()==False:
        print("★ifルート",res[num].isalpha(),res[num].isnumeric())
        ans+=res[num]
        print("ans",ans)
    elif res[num][0].isalpha() or res[num][0].isnumeric():
        print("☆elifルート",res[num][0].isalpha(),res[num][0].isnumeric())
        if res[num][-1].isalpha() or res[num][-1].isnumeric():
            print("☆☆elif→ifルート",res[num][-1].isalpha(),res[num][-1].isnumeric())
        ans+=" "+res[num]
    print("◆非該当")
print(ans)
