a=int(input("Digite o ano: "))

if (a% 4 == 0 and a% 100!=0) or (a%400==0):
    print("Ano é bissexto")
else:
    print("Ano não é bissexto")
