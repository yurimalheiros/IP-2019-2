# Função: Receber um número x e retornar os números pares de 1 até x
# Autor: Roberta de Lima Ribeiro

while True:

    numero =int(input('Digite um número: '))
    x = 0

    while x <= numero:
        if x % 2 == 0:
            print(x)
        x += 1
