num = int(input("Digite um número: "))
lista1 = []
lista2 = []

while (num != 0):
    lista1 = num
    lista2.append(lista1)
    num = int(input("Digite um número: "))

contagem = int(input("Quantas vezes se repete o: "))

print(lista2)
print()
print("O número", contagem,"se repete", lista2.count(contagem),"vezes.")
