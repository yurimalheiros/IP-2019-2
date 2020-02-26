#Função: Eliminar elementos repetidos
#Autor: Roberta de Lima Ribeiro

num = int(input('Digite um número:  '))
lista = []

while num != 0:
    lista.append(num)
    num = int(input('Digite um número:  '))
print(lista)

newlista = []

for i in range(len(lista)):
    if lista[i] not in newlista:
        newlista.append(lista[i])
print(newlista)
