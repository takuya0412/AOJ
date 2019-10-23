n = int(input())
num_list = [True]*(pow(10,8))
num_list[0]=False
for i in range(1,10000):
    if num_list[i]==False:
        continue
    div_num = num_list[i]-1
    tmp_cnt = 0
    while div_num >1:
        if num_list[i]%div_num==0:
            tmp_cnt+=1
            break
        div_num-=1
    if tmp_cnt==0:
