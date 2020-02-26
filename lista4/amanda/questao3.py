numero = float(input("Digite seu número: "))
lista = [ ]

maiorvalor = numero
menorvalor = 0

while numero != 0:
    lista.append(numero)

    if numero > maiorvalor:
        maiorvalor = numero

    elif numero < menorvalor:
            menorvalor = numero

    numero = float(input("Digite seu número: "))

print("Sua lista é: ", lista)
print("O maior valor é", maiorvalor, "e o menor valor é", menorvalor)

