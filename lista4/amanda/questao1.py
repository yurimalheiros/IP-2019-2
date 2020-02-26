lista = [ ]
numero = int(input("Digite seu número: "))
contador = 0

while contador < numero:

    if contador % 2 != 0:
        lista.append(contador)

    contador += 1
        
print("Os número ímpares são: ", lista)
