X = int(input())
contador = 1
tot = 0

while contador <= X:
    if X % contador == 0:
        tot += 1
    contador += 1
if tot == 2:
    print('O número {} é primo.'.format(X))
else:
    print('O número {} não é primo.'.format(X))
    
