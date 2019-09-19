i=0
data=[]
while i<50:
    try:
        data.append(list(map(lambda x:float(x),input().strip().split(','))))
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    
danger=[]
for j in range(len(data)):
    BMI=data[j][1]/data[j][2]**2
    if BMI>=25:
        print(int(data[j][0]))