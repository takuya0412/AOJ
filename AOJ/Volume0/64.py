sentence=[]
N=0
count=0
while True:
    try:
        sentence.append(input())
        count+=len(sentence[N])
        if count>10000:
            break
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    N+=1

ans=0
for j in range(N):
    x=""
    splitdata=[]
    for k in sentence[j]:
        if len(x)==0 and k.isnumeric():
            x+=k
        elif k.isnumeric() and x[-1].isnumeric():
            x+=k
        else:
            splitdata.append(x)
            x=""
            x+=k

    if len(x)!=0 and x.isnumeric():
        splitdata.append(x)
    #print(splitdata)
    numdata=[int(num) for num in splitdata if num.isnumeric()]
    #print(numdata)
    ans+=sum(numdata)
 
print(ans)
