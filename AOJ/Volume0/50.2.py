sen=list(input())
x=""
for i in range(len(sen)-4):
    x=sen[i]+sen[i+1]+sen[i+2]+sen[i+3]+sen[i+4]
    index=i
    if x=="apple":
        for j in "peach":
            sen[index]=j
            index+=1
    elif x=="peach":
        for j in "apple":
            sen[index]=j
            index+=1
            
print("".join(sen))
