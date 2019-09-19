import math
N=int(input())
i=0
while i<N:
    ran=[0]*11
    temp_list=['0']*8
    temp=""
    ran[0]=int(input())
    print(f"Case {i+1}:")
    for j in range(10):
        cnt=0
        temp=str(ran[j]**2)
        #print("temp",temp)
        for s in temp[::-1]:
            temp_list[7-cnt]=s
            cnt+=1
        #print("temp_list",temp_list)
        ran[j+1]=int("".join(temp_list[2:6]))
        temp_list=['0']*8
        print(ran[j+1])
    i+=1