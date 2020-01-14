soma = 0
contador = 0
n = int(input("Digite o numero (tecla 0 para fim)"))
while n>0:
    soma = soma + n
    contador = contador +1
    n = int(input("Digite o numero (tecla 0 para fim)"))
    print (n)
if contador>=1:
        print(soma + contador)