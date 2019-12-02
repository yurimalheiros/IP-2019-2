mes = int(input("Digite um mês (em numero) :"))
ano = int(input("Digite um ano (em numero) :"))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes ==10 or mes == 12:
    print (" Esse mês tem 31 dias!")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Esse mês tem 30 dias!")

elif mes == 2 and ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("Esse mês tem 29 dias!")
else:
    print("Esse mês tem 28 dias!")
        


