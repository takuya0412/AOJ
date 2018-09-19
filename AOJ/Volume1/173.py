for i in range(9):
    team,am,pm=input().split(' ')
    people=int(am)+int(pm)
    money=int(am)*200+int(pm)*300
    print(team,people,money)