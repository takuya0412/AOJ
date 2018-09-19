def calc(data):
    ans="d"
    for s in range(7):
        #print(s,"回目")
        
        if s%3==0:
            #print("if1")
            if (data[s]==data[s+1] and data[s]==data[s+2]) and data[s]!="s":
                #print("if1-1")
                ans=data[s]
                break
            
        if s<=2:
            #print("if1-elif")
            if (data[s]==data[s+3] and data[s]==data[s+6]) and data[s]!="s":
                #print("if1-elif1-if1")
                ans=data[s]
                break
            
        if (data[0]==data[4] and data[0]==data[8]) and data[0]!="s":
            #print("elif1")
            ans=data[0]
            break

        if (data[2]==data[4] and data[2]==data[6]) and data[2]!="s":
            #print("elif4")
            ans=data[2]

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
