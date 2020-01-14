contador = 1
contador2 = 1
while contador <= 9:
  print('-'*30)
  while contador2 <= 10:
    print('{}  x {:2}  =  {}'.format(contador, contador2, contador * contador2))
    contador2 += 1
  contador += 1
  contador2 = 1
