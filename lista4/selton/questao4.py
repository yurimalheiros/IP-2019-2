num = int(input("Digite um número: "))
lista1 = []
lista2 = []

while (num != 0):
    lista1 = num
    lista2.append(lista1)
    num = int(input("Digite um número: "))

lista2.sort()    
print(set(lista2))
