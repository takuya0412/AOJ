def calc(data):
    N=600/data
    ans=0
    for k in range(1,int(N)):
        ans+=data*(k*data)**2
    return ans

i=1
while i<=20:
    try:
        data = int(input())
        if data=="":
            break
        print(calc(data))
    except EOFError:
        break
    except IndexError:
        break
    except ValueError:
        break
