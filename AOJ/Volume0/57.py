i=0
while i<50:
    try:
        data=int(input())
        if data==0:
            break
        print(int((data**2+data+2)/2))
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
    i+=1

