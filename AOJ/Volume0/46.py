def calc(data):
    sdata=sorted(data)
    res=round(sdata[-1]-sdata[0],1)
    return res

i=0
data=[]
while i<50:
    try:
        #print("t1")
        data.append(float(input()))
        #print("ink",ink)
        if data[i]=="":
            break
    except EOFError:
        #print("error")
        break
    except IndexError:
        #print("error")
        break
    except ValueError:
        #print("error")
        break
    i+=1
#print("長さ",len(ink),ink)
print(calc(data))


    



