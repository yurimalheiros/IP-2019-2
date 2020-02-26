X = int(input("Digite um número"))
lista = []

for i in range(1 , X+1):
    if i %2 != 0:
        lista.append(i)

print(lista)
