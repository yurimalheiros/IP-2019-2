numero = int(input("Digite um numero:"))

if numero < 0:
    print("Numero invalido! Digitar numero posistivo!")
        
else:
    fatorial = 1    
    while numero > 1:
        fatorial = fatorial * numero
        numero = numero - 1
    print(fatorial)
        
