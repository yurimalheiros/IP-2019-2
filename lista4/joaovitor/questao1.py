entrada = int(input("Digite um número: "))
lista = []
contador = entrada

while contador != 0:
    
    if contador % 2 != 0:
        
        lista.append(contador)
        
    contador -= 1

lista.reverse()
print(lista)
