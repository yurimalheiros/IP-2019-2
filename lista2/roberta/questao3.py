# Função: Mostrar quantos dias tem em um mês
# Autor: Roberta de Lima Ribeiro

print("MOSTRAR QUANTOS DIAS TEM EM UM MÊS")
mes = int(input("Digite um mês"))
ano = int(input("Digite um ano"))

if mes > 0 and mes<= 12:
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print(30)
    else:
        if mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 and ano % 400 != 0:
                print(28)
            else:
                print(29)
        else:
                print(31)
else:
    print("Não existe no nosso calendário")

#1 - january - 31
#2 - february - 28
#3 - march - 31
#4 - april - 30
#5 - may - 31
#6 - june - 30
#7 - july - 31
#8 - august - 31
#9 - september - 30
#10 - octuber - 31
#11 - november - 30
#12 - december -31

print('Fim do programa')
