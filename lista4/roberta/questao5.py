#Função: Quantas vezes o número está presente na lista criada.
#Autor: Roberta de Lima Ribeiro

lista = []
num = int(input('Digite um número:  '))

while num != 0:
    lista.append(num)
    num = int(input('Digite um número:  '))
print(lista)

while True:
    checknum= int(input('Digite número para verificação:  '))
    rep = 0

    for i in range(len(lista)):
        if lista[i] == checknum:
            rep +=1

    if rep == 1:
        msg = 'vez'
    elif rep > 1:
        msg = 'vezes'
    elif rep == 0:
        rep = 'nenhuma'
        msg = 'vez'

    print('o numero de verificação foi encontrado', rep, msg) 
