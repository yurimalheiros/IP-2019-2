fim =int(input("digite um numero: "))
contador = 0

while contador<=fim:
    if contador % 2 == 0:
        print(contador)
        contador = contador+1
    else:
        contador = contador+1
        print("")
