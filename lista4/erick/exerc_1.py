numero = int(input("Digite um número: "))
lista = []
contador = 0

while contador <= numero:
  if contador % 2 != 0:
    lista.append(contador)
  contador = contador + 1
  print(lista)

