L = []
v = 0
i = str(input("Digite sim para continuar: "))

if i == "sim":
    while v == 0:
        valores = (int(input("Insira o dado para a lista: ")))
        if valores not in L:
            L.append(valores)
            if valores == 0:
                L.remove(0)
                print ("a lista contem os seguintes valores exceto dados repetidos", L)

else:
    print ("fim")