n=0
while n<20:
    n+=1
    try:
        candy=int(input())
        while True:
            if candy<39:
                break
            candy-=39
            
        if candy!=0 and candy<10:
            ans="0"+str(candy)
        elif candy==0:
            ans="39"
        else:
            ans=str(candy)
        print(f"3C{ans}")
    except ValueError:
        break
    except EOFError:
        break