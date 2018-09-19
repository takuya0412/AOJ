def func(date):
    days=[0,31,29,31,30,31,30,31,31,30,31,30]
    day_week=["Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday"]
    sum_days=sum(days[:date[0]])+(date[1])
    return day_week[sum_days%7-1]
    
i=0
while i<50:
    data=list(map(int,input().split(' ')))
    if data[0]==0:
        break
    print(func(data))
    i+=1

