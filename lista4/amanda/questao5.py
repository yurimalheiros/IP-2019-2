numero = int(input("Digite seu número: "))
lista = [ ]
contador1 = 0
contador2 = 0

while numero != 0:
    lista.append(numero)
    numero = int(input("Digite seu número: "))

numero = int(input("Digite o número a ser verficado: "))

while contador1 < len(lista):
    if lista [contador1] == numero:
        contador2 += 1
    contador1 += 1

print("O número está presente: ", contador2, "x")
