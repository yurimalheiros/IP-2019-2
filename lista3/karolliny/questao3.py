print("Questão 3")
numero = int (input("Digite um número: "))
contador1 = 1
primo = 0

while contador1 <= numero:
    if numero % contador1 == 0:
        primo+=1
    contador1+=1

if primo == 2:
    print("Número primo.")
else:
    print("O número não é primo.")
