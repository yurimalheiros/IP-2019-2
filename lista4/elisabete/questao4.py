num = int(input("Digite um número: "))
lista = []
contador1 = 0
contador2 = 0
while num != 0:
    lista.append(num)
    num = int(input("Digite um número: "))

while contador1 < len(lista) - 1:
    contador2 = contador1 + 1

    while contador2 < len(lista):
        if lista[contador1] == lista[contador2]:
            lista.pop(contador2)

        else:
            contador2 += 1
    contador1 += 1
    print("A lista é: ", lista)
