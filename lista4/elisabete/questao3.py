num = int(input("Digite um número: "))
lista = []
maior_numero = num
menor_numero = 0
while num != 0:
    lista.append(num)

    if num > maior_numero:
        maior_numero = num

    elif num < menor_numero:
        menor_numero = num
    
    num = int(input("Digite um número: "))
print("Sua lista é: ", lista)
print("Maior número é: ", maior_numero, "e o menor número é: ", menor_numero)
