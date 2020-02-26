X = int(input("Digite um número"))
lista = []

while X != 0:
    for chave , elemento in enumerate(lista):
        if X < elemento:
            lista.insert(chave , X)
            break

    else:
        lista.append(X)
    X = int(input("Digite um número"))

print(lista)
