numero = int(input("Digite um número: "))
contador = 1

while contador <= numero:
    if numero % 2 == 1:
        contador = contador + 1
        print(numero, "é primo")
        break
    else:
        print(numero, "não é primo")
        break
