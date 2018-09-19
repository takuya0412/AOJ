i=1
while i<200:
    count=1
    try:
        array = list(map(lambda x:int(x),input().strip().split()))
        if array[0]=="":
            break
        s=sum(array)

        while True:
            s/=10
            if s<1:
                break
            count+=1
        print(count)
        i+=1

    except EOFError:
        break
    except IndexError:
        break
