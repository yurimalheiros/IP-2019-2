n = int(input("Digite seu número: "))
nao_primo = 0
numero_atual = 2

while numero_atual < n:
    if n % numero_atual == 0:
        nao_primo += 1
        
    
    numero_atual += 1

if nao_primo == 0:
    print("É primo.")

else:
    print("Não é primo.")
