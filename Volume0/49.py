import collections
i=0
data=[]
while i<50:
    try:
        data.append(list(input().strip().split(','))[1])
        if data[i]=="":
            break
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    i+=1
count_dict=dict(collections.Counter(data))
a=count_dict.get("A",0)
b=count_dict.get("B",0)
ab=count_dict.get("AB",0)
o=count_dict.get("O",0)
print(a)
print(b)
print(ab)
print(o)

