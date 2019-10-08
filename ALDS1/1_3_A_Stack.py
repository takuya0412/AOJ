operand = ["+", "-", "*"]
in_data = input().strip().split(" ")
res_stack = []
for data in in_data:
    if data not in operand:
        res_stack.append(int(data))
    else:
        b = res_stack.pop()
        a = res_stack.pop()
        res = eval("a{}b".format(data))
        res_stack.append(res)
print(res_stack.pop())
