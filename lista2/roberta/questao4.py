# Função: Números inteiros em ordem crescente
# Autor: Roberta de Lima Ribeiro

print('NÚMEROS INTEIROS EM ORDEM CRESCENTE')

n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
n3 = int(input('Digite mais um número'))

if n1>n2 and n1>n3:
    if n2>n3:
        print(n3,n2,n1)
    else:
        print(n1,n3,n2)
elif n2>n1 and n2>n3:
    if n1>n3:
        print(n3,n1,n2)
    else:
        print(n1,n3,n2)
elif n3>n1 and n3>n2:
    if n1>n2:
        print(n2,n1,n3)
    else:
        print(n1,n3,n2)
else:
        print('iguais')
print('Fim do programa')
