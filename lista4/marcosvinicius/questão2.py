n = []
pause = 0
while pause == 0:
    n1 = int(input('Digite um número: '))
    n.append(n1)
    if n1 == 0:
        n.remove(0)
        print(n)
