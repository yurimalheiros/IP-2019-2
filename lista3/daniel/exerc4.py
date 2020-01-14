total = 0

while True:
  numero = int(input('Digite um número -> '))
  if numero != 0:
    total += numero
  else:
    break
print('\33[32mTotal = {}'.format(total), end='')
