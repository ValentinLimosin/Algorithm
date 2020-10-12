def hanoi(x,start,middle,end):
    if x > 0:
        hanoi(x-1,start,end,middle)
        print(start+"  vers  "+end)
        hanoi(x-1,middle,start,end)

hanoi(eval(input("entré le nombre de disque utlisé : ")),"A","B","C")
