n=0
data=[]
while n<40:
    n+=1
    try:
        data.append(list(map(lambda x:float(x),input().split(' '))))
    except ValueError:
        break
    except EOFError:
        break
cnt_l=[0]*4
cnt_r=[0]*4
for l in data:
    if 1.1<=l[0]:
        cnt_l[0]+=1
    elif 0.6<=l[0]<1.1:
        cnt_l[1]+=1
    elif 0.2<=l[0]<0.6:
        cnt_l[2]+=1
    else:
        cnt_l[3]+=1
for r in data:
    if 1.1<=r[1]:
        cnt_r[0]+=1
    elif 0.6<=r[1]<1.1:
        cnt_r[1]+=1
    elif 0.2<=r[1]<0.6:
        cnt_r[2]+=1
    else:
        cnt_r[3]+=1
for j in range(4):
    print(cnt_l[j],cnt_r[j])
