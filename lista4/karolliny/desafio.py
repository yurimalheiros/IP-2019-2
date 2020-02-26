print ("Desafio")
numero = int(input("Digite um número: "))
lista = []

while (numero != 0):
    lista.append (numero)
    numero = int(input("Digite um número: "))

for x in range(len(lista),0,-1):
    for indice in range (0, x-1):
        if lista[indice] > lista[indice+1]:
            lista[indice+1], lista[indice] = lista[indice], lista[indice+1]

print (lista)
