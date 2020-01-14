acumulador = 0
n = -1

print("Digite zero '0' quando quiser finalizar a soma")

while n != 0:
    n = float(input("Digite o preço da compra:"))
    acumulador = acumulador + n
    
print("Seu gasto total foi de:", acumulador)
