def calc(data):

    ans=""
    for s in range(7):
        if s%3==0:
            if (data[s]==data[s+1] and data[s]==data[s+2]) and data[s]!="s":
                ans=data[s]
                break
            
        if s<=2:
            if (data[s]==data[s+3] and data[s]==data[s+6]) and data[s]!="s":
                ans=data[s]
                break
            
        elif (data[0]==data[4] and data[0]==data[8]) and data[0]!="s":
            ans=data[0]
        
        elif (data[2]==data[4] and data[2]==data[6]) and data[0]!="s":
            ans=data[2]
        
        else:
            ans="d"
    
    
    return ans

            

i=1
while i<=50:
    try:
        data = input()
        if data=="":
            break
        print(calc(data))
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
