N=0
while N<200:
    N+=1
    d=input()
    if d=="0":
        break
    card=list(map(int,d.split(' ')))
    card.sort(reverse=True)
    one=card.count(1)
    cards=[ i for i in card if i!=1]
    point=0
    for i in cards:
        if 10<=i<=13:
            point+=10
        elif 2<=i<=9:
            point+=i
    point+=one
    if point>21:
        point=0
    elif one>=1:
        if point<=21:
            for i in range(one):
                if point+10>21:
                    break
                point+=10
    print(point)
            
        
        