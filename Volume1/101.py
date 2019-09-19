N=int(input())
i=0
while i<N:
    cnv=list(input())
    if cnv=="":
        break
    for s in range(len(cnv)-6):
        if "".join(cnv[s:s+7])=="Hoshino":
            cnv[s+6]="a"
    print("".join(cnv))
    i+=1
            