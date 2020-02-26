#Função: Digitação de números até 0, lista criada e exibição de todos elementos.
#Autor: Roberta de Lima Ribeiro.
while True:
    lista = []
    num = int(input('Digite um número: '))

    while num != 0:
        lista.append(num)
        num = int(input('Digite um número: '))
    print(lista)
