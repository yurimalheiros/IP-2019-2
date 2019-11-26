ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês em numero: "))

if (ano % 4 == 0) and (ano % 100 != 0):
    if (mes == 1)or(mes == 3)or(mes == 5)or(mes == 7)or(mes == 8)or(mes == 10)or(mes == 12):
        print("Esse mês tem 31 dias")
    elif (mes == 4)or(mes == 6)or(mes == 9)or(mes == 11):
        print("Esse mês tem 30 dias")
    else:
        print("Esse mês tem 29 dias")
else:
    if (mes == 1)or(mes == 3)or(mes == 5)or(mes == 7)or(mes == 8)or(mes == 10)or(mes == 12): 
        print("Esse mês tem 31 dias")
    elif (mes == 4)or(mes == 6)or(mes == 9)or(mes == 11):
        print("Esse mês tem 30 dias")
    else:
        print("Esse mês tem 28 dias")
