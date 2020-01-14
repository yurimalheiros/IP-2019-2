# Função: Receber um número x e retornar o resultado de x!
# Autor: Roberta de Lima Ribeiro

while True:

    numero = int(input('Digite um número: '))
    contador = 1
    fatorial = 1

    while contador <= numero:
        fatorial = fatorial * contador
        contador += 1
    print(fatorial)
