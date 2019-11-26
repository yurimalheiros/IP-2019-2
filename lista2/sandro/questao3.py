mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("O mês digitado têm 30 dias neste ano.")
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("O mês digitado têm 31 dias neste ano.")
else:
    if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
        print("O mês de fevereiro têm 29 dias neste ano.")
    else:
        print("O mês de fevereiro têm 28 dias neste ano.")
