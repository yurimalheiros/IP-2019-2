n = []
pause = 0
while pause == 0:
    n1 = int(input('Digite um número: '))
    n.append(n1)
    if n1 == 0:
        n.sort()
        n.remove(0)
        print('A ordem da lista é : {}'.format(n))
        print ("O menor número da lista é: {}".format(n[0]))
        print('o maior número da lista é: {}'.format(n[-1]))
