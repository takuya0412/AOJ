N=0
count=0
while N<50:
    try:
        N+=1
        s=list(input())
        r=s[::-1]
        if s==[]:
            break
        elif s==r:
            count+=1

    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
print(count)
