# Função: Exibir tabuada de 1 a 9
# Autor: Roberta de Lima Ribeiro

while True:   
    num1 = 1
    num2 = 1
    operacao = int(input(
"""
TABUADA
1. Adição
2. Multiplicação
3. Subtração
4. Divisão
5. Sair
Escolha uma operação: """))

    while num1 <= 9:
        while num2 <= 10:
            if operacao == 1:
                resultado = num1 + num2
                exibe = '{} + {} = {}'.format(num1,num2, resultado)
            elif operacao == 2:
                resultado = num1 * num2 
                exibe = '{} x {} = {}'.format(num1,num2, resultado)
            elif operacao == 3:
                resultado = (num1 + num2) - num1
                exibe = '{} - {} = {}'.format(num2+num1,num1, resultado)
            elif operacao == 4:
                resultado = (num1*num2) / num1
                exibe = '{} / {} = {}'.format(num2*num1,num1, resultado)
            else :
                exit()
            print(exibe)
            num2 += 1
        print('')
        num2 = 1
        num1 += 1

