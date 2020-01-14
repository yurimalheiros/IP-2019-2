number = int(input('Digite o número: '))
counter = 0
for n in range(1, number + 1):
    if number % n == 0:
        counter = counter + 1
if counter == 2:
    print('É primo')
else:
    print('Não é primo')
