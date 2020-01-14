x = int(input("Digite um número inteiro não-negativo: "))
contador = 1
x_fat = 1
while contador <= x:
    x_fat = x_fat * contador 
    contador = contador + 1
print("%d! = %d" %(x, x_fat))
