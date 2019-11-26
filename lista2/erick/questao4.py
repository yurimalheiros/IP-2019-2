'''
4) Escreva um programa que receba três números inteiros e exibe eles em ordem
crescente.
'''
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite  mais um valor: "))
n3 = int(input("Digite outra: "))



# TODO: tenho que fazer
maior = 0

if (n1 >= n2):
    maior = n1
    if(n1 >= n3):
        maior = n1
    else:
        maior = n3


# if (n1 < n2 and n1 < n3):
#     primeiro = n1
# elif (n2 < n1 and n2 < n3):
#     primeiro = n2
# elif (n3 < n1 and n3 < n2):
#     primeiro = n3

# if (n1 == primeiro):
#     if (n2 < n3):
#         segundo = n2
#     else: 
#         segundo = n3

# elif (n2 == primeiro):
#     if (n1 < n3):
#         segundo = n1
#     else:
#         segundo = n3

# elif (n3 == primeiro):
#     if (n1 < n2):
#         primeiro = n1
#     else:
#         primeiro = n2
