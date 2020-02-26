print ("Questão 5")
numero = int(input("Digite um número: "))
lista = []

while (numero != 0):
    lista.append (numero)
    numero = int(input("Digite um número: "))

print (lista)

numerob = int(input("Digite o número: "))
cont = 0

for x in lista:

    if x == numerob:
        cont += 1

print("O número {} aparece {} vez(es)" .format(numerob, cont))