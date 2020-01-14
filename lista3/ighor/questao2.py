numero = int(input("Qual o fatorial"))
contador = 1
fatorial = 1

while contador <= numero:
    fatorial = fatorial * contador
    contador += 1

print(fatorial)
