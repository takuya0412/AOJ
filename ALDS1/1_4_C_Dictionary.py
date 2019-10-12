N = int(input())
dic = []
res = []

def find_dic(val):
    global dic
    for i in dic:
        if i == val:
            return "yes"
    return "no"

for i in range(N):
    cmd, val = input().strip().split(' ')
    if cmd == "insert":
        dic.insert(0,val)
    else:
        res.append(find_dic(val))
for i in res:
    print(i)

