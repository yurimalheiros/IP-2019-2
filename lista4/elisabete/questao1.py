x = int(input("Digite um número: "))
lista = []
contador = 0
while contador < x:
    if contador % 2 != 0:
        lista.append(contador)
    contador += 1
print("Os números ímpares são: ", lista)
    
