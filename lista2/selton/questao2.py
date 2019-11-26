ano = int(input("Digite o ano: "))

if (ano % 4 == 0) or (ano % 400 == 0):
    print("Esse ano é bissexto.")

elif (ano % 100 != 0):
    print("Esse ano não é bissexto.")
 

