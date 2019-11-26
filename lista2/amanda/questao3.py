mes=int(input("Digite o  número do seu respectivo mês: "))
ano=int(input("Digite o ano: "))

if (mes==4) or (mes==6) or (mes==9) or (mes==11):
    print("O mês tem 30 dias.")
else:
    if mes == 2:  
        if  ano%4 == 0 or ano%100 != 0  and ano%400 == 0:
            print("O mês tem 29 dias.")
        else:
            print("O mês tem 28 dias.")
    else:
        if (mes==1) or (mes==3) or (mes==5) or (mes==7) or (mes==8) or (mes==10) or (mes==12):
            print("O mês tem 31 dias.")

if (ano%4==0 and ano % 100!=0) or (ano%400==0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto.")
    
