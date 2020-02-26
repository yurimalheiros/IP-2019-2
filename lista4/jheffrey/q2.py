op = input("Digite 0 para finalizar: ")
while op != "0":
    num = int(input("Digite o numero: "))
    valores = list(range(1, num))
    print (valores)
    x = input("Digite 0 para finalizar: ")
    if x == "0":
        print ("fim")
        break