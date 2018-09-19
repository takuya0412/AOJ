def search():
    
    return

import re
data2=[]
data=input()
print("文字列長さ",len(data))
for i in range(len(data)-3):
    print("i",i,"data[i+4]",data[i:i+4])
    if data[i:i+4].isalpha() and data[i+4].isalpha()==False and data[i-1].isalpha()==False:
        print("if",data[i:i+4])
        data2.append(data[:i+4])
print("data2",data2)
for i in range(len(data)-4):
    print("i",i,"data[i+5]",data[i:i+5])
    if data[i:i+5].isalpha() and data[i+5].isalpha()==False and data[i-1].isalpha()==False:
        data2.append(data[:i+5])
print("data2",data2)
for i in range(len(data)-5):
    if data[i:i+6].isalpha() and data[i+6].isalpha()==False and data[i-1].isalpha()==False:
        data2.append(data[:i+6])

print("".join(data2))
