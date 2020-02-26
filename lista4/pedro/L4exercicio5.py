
lista_vazia= list()
numero = int(input("Digite um número: "))  
while numero != 0:
  lista_vazia.append(numero)
  numero = int(input("Digite um número: "))
repetido = int(input("Digite um número repetido: "))
print(repetido, lista_vazia.count(repetido))