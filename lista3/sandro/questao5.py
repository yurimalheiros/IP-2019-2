tabuada = 1
numero = 1

while tabuada <= 9:
    print("%d x %d = %d" % (tabuada, numero, tabuada * numero))
    numero = numero + 1
    if numero == 11:
        numero = 1
        tabuada = tabuada + 1
