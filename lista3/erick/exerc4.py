numero = int(input("Digite um valor: "))
total = 0
resUser = True
while (resUser):
    if (numero == 0):
        resUser = False
    elif (numero != 0):
        total = total + numero
        numero = int(input("Digite um valor: "))
print(total)
