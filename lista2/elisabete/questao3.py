mes = int(input("digite o nome do mês ou o número do mês"))
ano = int(input("digite um ano"))
if mes == 2 or mes == "fevereiro" and ano % 4 == 0 or 100 != 0 and 400 == 0:
    print(f"o mês {mes} tem 29 dias")
else:
    print(f"o mes {mes} tem 28 dias")
if(mes == 1 or mes == "janeiro") or (mes == 3 or mes == "março") or (mes == 5 or mes == "maio") or (mes == 7 or mes == "julho") or (mes == 8 or mes == "agosto") or (mes == 10 or mes == "outubro") or (mes == 12 or mes == "dezembro"):
    print(f"o mes {mes} tem 31 dias")
elif(mes == 4 or mes == "abril") or (mes == 6 or mes == "junho") or (mes == 9 or mes == "setembro") or (mes == 11 or mes == "novembro"):
    print("o mes {mes} tem 30 dias")
if(ano % 4 == 0 and ano % 100 != 0) or (ano %400 == 0):
    print("o {ano} ano é bissexto")
else:
    print("o ano {ano} não é bissexto")
