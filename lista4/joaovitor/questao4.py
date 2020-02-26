entrada = int(input("Digite um número: "))
lista = []
lista.append(entrada)

while entrada != 0:
    
    entrada = int(input("Digite outro: "))
    
    if entrada in lista:
        print()
    else:
        lista.append(entrada)
        
lista.sort()
print(lista)
    
