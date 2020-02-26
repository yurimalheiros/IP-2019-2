#Função:  Criando lista com os números ímpares de 1 até x.
#Autor: Roberta de Lima Ribeiro.

while True:
    lista = []
    num= int(input("Digite um número:  "))
    ind= 0

    while ind <= num:
        if ind % 2 != 0:
            lista.append(ind)
        ind+=1
    print(lista)
