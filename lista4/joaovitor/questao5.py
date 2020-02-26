entrada = int(input("Digite um número: "))
lista = []
repete = 0
lista.append(entrada)

while entrada != 0:
    
    entrada = int(input("Digite outro: "))
    
    if entrada in lista:
        lista.append(entrada)
        print(entrada, "já esta na lista")
        repete += 1
    else:
        lista.append(entrada)
        
lista.sort()        
print("O numeros da lista", lista, "se repetem", repete,"vezes")

    
