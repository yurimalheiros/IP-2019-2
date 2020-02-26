numero = 2
lista = []
while numero != 0:
    numero = int(input("Digite um número de 0 a 9: "))
    if(numero != 0): 
        lista.append(numero)
maxValue = lista[0] 
minValue = lista[0]
for numero in lista:
    if numero > maxValue:
        maxValue = numero
    if numero < minValue:
        minValue = numero
print(maxValue)
print(minValue)
