a = int(input("Digite o numero "))
contador = 1
fat = 1
while contador <= a:
    fat = fat * contador
    contador = contador + 1
print (a,"!", fat)