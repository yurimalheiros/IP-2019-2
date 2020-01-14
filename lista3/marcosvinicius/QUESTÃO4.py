reset = 's'
while reset == 's':
    n = 1
    soma = 1
    while n!= 0:
        n= int(input('DIGITE UM NÚMERO [DIGITAR 0 ENCERRARÁ A SOMA] : '))
        soma += n
    print ('O RESULTADO DA SOMA É {} !  '.format(soma-1))
    reset = input("DESEJAR INSERIR OUTROS NÚMEROS? [DIGITE s PARA REFAZER] : ")
