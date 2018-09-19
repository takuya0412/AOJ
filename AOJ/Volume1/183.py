while True:
    d=""
    ans="NA"
    brk=0
    for j in range(3):
        d+=input()
        if "0" in d:
            brk=1
            break
    if brk==1:
        break
    if d[0]==d[4]==d[8] and d[0]!="+":
            ans=d[0]
    if d[2]==d[4]==d[6] and d[2]!="+":
            ans=d[2]
    for n in range(3):
        if d[n]==d[n+3]==d[n+6] and d[n]!="+":
            ans=d[n]
        if d[n*3]==d[n*3+1]==d[n*3+2] and d[n*3]!="+":
            ans=d[n*3]
    print(ans)