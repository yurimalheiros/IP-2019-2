X = int(input("Digite um número"))
lista = []

cont1 = 0
cont2 = 0

while X != 0:
    lista.append(X)
    X = int(input("Digite um número"))

X = int(input("Verifique o número"))
while cont1 < len(lista):
    if lista[cont1] == X:
        cont2 += 1
    cont1 += 1

print(cont2)
              
