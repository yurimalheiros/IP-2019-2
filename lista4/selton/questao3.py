num = int(input("Digite um número: "))
lista1 = []
lista2 = []

while (num != 0):
    lista1 = num
    lista2.append(lista1)
    num = int(input("Digite um número: "))
    
print ("Excluindo o 0, o menor elemento é: " , min(lista2))
print ("O maior elemento é: " , max(lista2))
