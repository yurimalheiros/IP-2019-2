# Função: Retornar se o número é primo ou não
# Autor: Roberta de Lima Ribeiro

while True :
    
    num = int(input('Digite um número: '))
    contador = 0
    incremento = 1

    if num > 1:
        while incremento <= num:
            if num % incremento == 0:
                contador += 1
            incremento += 1
        if contador == 2:
            print(num,' é um número primo')
        else:
            print(num,' não é um número primo')
    else:
        print(num,' não é um número primo')
    
