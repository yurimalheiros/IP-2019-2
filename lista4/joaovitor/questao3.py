entrada = int(input("Digite um número: "))
lista = []
while entrada != 0:
    
    lista.append(entrada)
    
    entrada = int(input("Digite outro: "))

lista.sort()

maior = len(lista)-1

print("O menor valor é", lista[0], "e o maior é", lista[maior])
