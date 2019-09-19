prime_list=[True]*1000000
prime_list[0]=False
prime_list[1]=False
for i in range(2,1000000):
    if prime_list[i]==False:
        continue
    elif prime_list[i]==True and i<1000:
        cnt=i
        while i*cnt<1000000:
            prime_list[i*cnt]=False
            cnt+=1

            

i=1
while i<=30:
    try:
        data = int(input())
        res=prime_list[:data+1].count(True)
        #print(prime_list[:data])
        print(res)
        i+=1
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
