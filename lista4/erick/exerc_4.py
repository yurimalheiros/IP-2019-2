valor = int(input("Digite um valor: "))
lista = []
contador = 0
contador2 = 0

while valor != 0:
  lista.append(valor)
  valor = int(input("Digite outro valor: "))

while contador < len(lista) - 1:
  contador2 = contador + 1
  while contador2 < len(lista):
    if lista[contador] == lista[contador2]:
      lista.pop(contador2)
    else:
      contador2 = contador2 + 1
  contador = contador + 1
print(lista)