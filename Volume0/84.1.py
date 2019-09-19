def search():
    
    return

import re
data2=[]
data=input()
data=re.split("[,.]",data)
print("data:",data)
data1=" ".join([i for i in data if i!=" "]).split(' ')
print("data1:",data1)
for k in data1:
    if 3<=len(k)<=6 and k.isalpha():
        data2.append(k)
print(data2)
print(" ".join(data2))

