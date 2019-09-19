data=list(map(lambda x:int(x),input().split(' ')))
TUBO=3.305785
print(round((data[0]*data[1])/TUBO,8))