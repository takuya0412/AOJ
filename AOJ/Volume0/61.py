def calc(data,point,q):
    rank=list(set(point))
    rank.sort(reverse=True)
    ans=[]
    for num  in q:
        ans.append(rank.index(data[num-1][1])+1)
    return ans

i=0
data=[]
point=[]
q=[]
while i<100:
    try:
        data.append(list(map(lambda x:int(x),input().strip().split(','))))
        point.append(data[i][1])
        if data[i][0]==0 and data[i][1]==0:
            data.pop()
            point.pop()
            break
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    
i=0
while i<1000:
    try:

        q.append(int(input()))
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break

res=calc(data,point,q)

for answer in res:
    print(answer)
    




