numero = int(input("Digite um valor: "))
contador = 1
total = 0
while contador <= numero:
    if numero % contador == 0:
        total = total + 1
    contador += 1
if total == 2:
    print("Ele é primo")
else:
    print("Ele não é primo.") 
        