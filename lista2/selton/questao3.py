ano = int(input("Digite o ano: "))

if (ano % 4 == 0) or (ano % 400 == 0):
    print("Esse ano é bissexto.")
    print()
    mes = str.lower(input("Digite o mês: "))
    if (mes == "janeiro") or (mes == "março") or (mes == "maio") or (mes == "julho") or (mes == "agosto") or (mes == "outubro") or (mes == "dezembro"):
        print(mes, "tem 31 dias")

    elif (mes == "abril") or (mes == "junho") or (mes == "setembro") or (mes == "novembro"):
        print(mes, "tem 30 dias")

    if (mes == "fevereiro"):
        print(mes, "tem 29 dias")
    
elif (ano % 100 != 0):
    print("Esse ano não é bissexto.")
    print()
    mes = str.lower(input("Digite o mês: "))
    if (mes == "janeiro") or (mes == "março") or (mes == "maio") or (mes == "julho") or (mes == "agosto") or (mes == "outubro") or (mes == "dezembro"):
        print(mes, "tem 31 dias")

    elif (mes == "abril") or (mes == "junho") or (mes == "setembro") or (mes == "novembro"):
        print(mes, "tem 30 dias")

    elif (mes == "fevereiro"):
        print(mes, "tem 28 dias")

 



