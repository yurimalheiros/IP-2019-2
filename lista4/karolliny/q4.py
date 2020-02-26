print ("Questão 4")
numero = int(input("Digite um número: "))
lista = []

while (numero != 0):
    lista.append (numero)
    numero = int(input("Digite um número: "))
print(lista)

list = []
for x in lista:

    if x not in list:
        list.append(x)

print(list)