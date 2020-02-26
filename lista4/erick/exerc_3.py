valor = int(input("Digite um valor: "))
lista = []
contador = 0

maior = 0
menor = 0

while valor != 0:
  lista.append(valor)
  if contador == 0:
    maior = menor = valor
  else:
    if valor > maior:
      maior = valor
    if valor < menor:
      menor = valor
  
  contador = contador + 1

  valor = int(input("Digite um valor: "))

print('Maior: {}\nMenor: {}'.format(maior, menor))
print('Lista: {}'.format(lista))