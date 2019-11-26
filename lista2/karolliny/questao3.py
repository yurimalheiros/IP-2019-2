print ("Questão 3")
mes,ano = map(int,input("Digite um mês e o ano: ").split())

if mes > 0 and mes <= 12:
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        print(30)
    else:
        if mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 != 0:
                print(28)
            else:
                print(29)
        else:
            print(31)
else:
    print("Não existe no nosso calendário")

#1  - janeiro   - 31
#2  - fevereiro - 28 | 29
#3  - março     - 31
#4  - abril     - 30
#5  - maio      - 31
#6  - junho     - 30
#7  - julho     - 31

#8  - agosto    - 31
#9  - setembro  - 30
#10 - outubro   - 31
#11 - novembro  - 30
#12 - dezembro  - 31
    
