number = int(input('Digite um número: '))
counter = number
factorial = 1
while counter > 0:
    print(counter)
    factorial = factorial * counter
    counter = counter - 1
print(f'O {number}! é = {factorial}')