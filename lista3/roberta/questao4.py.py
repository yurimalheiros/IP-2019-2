# Função: Receber uma sequência e receber a soma de todos os números
# Autor: Roberta de Lima Ribeiro


soma = 0
num = 1

while num != 0:
    num = int(input('Digite um número: '))

    soma += num
    
print('Soma: ', soma)
