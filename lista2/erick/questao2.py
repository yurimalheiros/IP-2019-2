'''
 2) Escreva um programa que recebe um ano como entrada e verifica se esse ano
é bissexto.
'''
ano = int(input("Digite um valor: "))
if (ano % 4 and ano % 400):
    print(ano, " é bissexto")
else:
    print(ano, "nao é bissexto")

