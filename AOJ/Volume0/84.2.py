import re
data2=[]
data=input()
if len(data)>1024:
    data=data[:1025]
data=re.split("[,. ]",data)
#print("data:",data)
for k in data:
    if 3<=len(k)<=6:
        data2.append(k)
#print(data2)
print(" ".join(data2))

