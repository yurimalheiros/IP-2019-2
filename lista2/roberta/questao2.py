# Função: Calcular se um ano é bissexto
# Autor: Roberta de Lima Ribeiro

print('CALCULAR SE UM ANO É BISSEXTO')

ano = int(input('Digite um ano'))

if ano%4==0:
    print('ano é bissexto')
elif ano%100==0:
    print('é bissexto')
else:
    print('não bissexto')
print('fim do programa')
    
