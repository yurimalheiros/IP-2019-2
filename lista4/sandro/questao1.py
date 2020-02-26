numero = int(input("Digite um número: "))
indice = 1

while indice <= numero:
    if indice % 2 != 0: 
        print(indice)
    elif indice == numero:
        print(indice)
      
    indice = indice + 1
