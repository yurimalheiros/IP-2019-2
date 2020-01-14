print("Questão 5")
cont1 = 1
contador2 = 1

while cont1 <= 9:
    print('-'*12)
    while contador2 <= 10:
        print('{} x {:2} = {}'.format(cont1, contador2, cont1 * contador2))
        contador2+=1
    contador2=1
    cont1+=1