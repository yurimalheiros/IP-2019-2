entrada = int(input("digite um número: "))

while entrada != 0:
    if (entrada == 2)or(entrada == 3)or(entrada == 5)or(entrada == 7)or(entrada == 11):
        print("esse número é primo")
        entrada = int(input("digite 0 para sair ou outro número para continuar: "))
    elif (entrada % 2 == 0)or(entrada % 3 == 0)or(entrada % 5 == 0)or(entrada % 7 == 0)or(entrada % 11 == 0):
        print("esse numero não é primo")
        entrada = int(input("digite 0 para sair ou outro número para continuar: "))
    else:
        print("esse número é primo")
        entrada = int(input("digite 0 para sair ou outro número para continuar: "))
print("fim")
