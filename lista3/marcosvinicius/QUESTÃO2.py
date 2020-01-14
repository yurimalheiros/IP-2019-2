n1 = int(input('digite um número: '))
fatorial = 1
contador = 2
while contador <=n1:
        fatorial = fatorial * contador 
        contador += 1
print ('O fatorial de {} é {} !'.format(n1,fatorial))
