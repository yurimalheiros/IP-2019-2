#Função: "a partir do código 2",menor e maior valor da lista criada
#Autor: Roberta de Lima Ribeiro

while True:
    lista = []
    num = int(input('Digite um número:  '))

    while num != 0:
        lista.append(num)
        num = int(input('Digite um número:  '))
    print(lista)

    menor= 9999
    maior=-9999
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]

        if lista[i] > maior:
            maior = lista[i]

    print('maior', maior)
    print('menor', menor)
