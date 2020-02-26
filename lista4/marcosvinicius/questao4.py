n = []
pause = 0
while pause == 0:
    n1 = int(input('DIGITE UM NÚMERO:'))
    if n1 not in n:
        n.append(n1)
        if n1 == 0:
            n.remove(0)
            n.sort()
            print(n)
