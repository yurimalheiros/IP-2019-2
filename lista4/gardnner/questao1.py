num= int(input('digite um numero: '))
lista= [ ]
cont= 0
while cont <= num:
    if cont % 2 != 0:
        lista.append(cont)
    cont += 1
print (lista) 