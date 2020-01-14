print("Questão 2")
num = int(input("Digite um número: "))
fatorial = 1
i = 1

while i <= num:
    fatorial = fatorial*i
    i = i + 1
print("Fatorial de",num,"é",fatorial)
