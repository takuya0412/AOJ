while True:
    record=input()
    if record=="0":
        break
    pA=record[1:].count("A")
    pB=record[1:].count("B")
    if pA>pB:
        pA+=1
    else:
        pB+=1
    print(pA,pB)