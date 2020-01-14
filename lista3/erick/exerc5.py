contadorI = 1
contadorJ = 1

while contadorI <= 9:
  print('-'*12)
  while contadorJ <= 10:
    print('{}  x {:2}  =  {}'.format(contadorI, contadorJ, contadorI * contadorJ))
    contadorJ += 1
  contadorI += 1
  contadorJ = 1
