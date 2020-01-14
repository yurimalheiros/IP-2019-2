contador1 = 1
contador2 = 1

while contador1 <= 9:
    print('-'*12)
    while contador2 <= 10:
        print('{} x {:2} = {}'.format(contador1, contador2, contador1 * contador2))
        contador2 += 1
    contador2 = 1
    contador1 += 1
