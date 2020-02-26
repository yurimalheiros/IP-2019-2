valor = int(input("Digite um numero: "))
lista = []
contador = 0
contador2 = 0

while valor != 0:
  lista.append(valor)
  valor = int(input("Digite um outro numero: "))

valor = int(input('\nDigite mais um outro numero: '))
while contador < len(lista):
  if lista[contador] == valor:
    contador2 += 1
  contador+=1
print(contador2)