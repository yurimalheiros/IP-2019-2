numero = 2
lista = []
while numero != 0:
    numero = int(input("Digite um número de 0 a 9: "))
    if(numero != 0): 
        lista.append(numero)

for numero in lista:
    if numero == numero:
        lista.remove(numero)
print(lista)
