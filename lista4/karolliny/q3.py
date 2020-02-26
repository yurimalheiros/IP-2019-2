print ("Questão 3")
numero = int(input("Digite um número: "))
lista = []

while (numero != 0):
    lista.append (numero)
    numero = int(input("Digite um número: "))
    
lista.sort()
print(lista)
print ("O menor valor é: {} , o maior valor é: {}" .format(lista[0], lista[-1]))
