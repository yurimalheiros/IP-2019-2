lis = []
acumulador = 0
i = str(input("Digite 'sim' para continuar: "))

if i == 'sim':

    while acumulador == 0:
        print ("Digite 0 para parar")
        tolis = int(input("Digite o valor: "))
        lis.append(tolis)
        if tolis == 0:
            lis.pop(-1)
            print(lis)
            toc = int(input("valor a ser consultado: "))
            print("o valor aparece:",(lis.count(toc)))
else:
    print ("fim")