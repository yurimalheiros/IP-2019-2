numero = 2
lista = []

while numero != 0:
    numero = int(input("Digite um número de 0 a 9: "))
    if(numero != 0): 
        lista.append(numero)
    if numero in lista:
        print(lista.count(numero))


