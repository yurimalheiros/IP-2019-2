n1 = float(input("Digite o Primeiro Numero:"))
n2 = float(input("Digite o Segundo Numero:"))
n3 = float(input("Digite o Terceiro Numero:"))

if n1 > n2 and n1 > n3 and n2 > n3:
    print(n1,n2,n3)

if n1 > n2 and n1 > n3 and n2 < n3:
    print(n1,n3,n2)

if n2 > n1 and n2 > n3 and n1 > n3:
    print(n2,n1,n3)

if n2 > n1 and n2 > n3 and n1 < n3:
    print(n2,n3,n1)

if n3 > n1 and n3 > n2 and n1 > n2:
    print(n3,n1,n2)

if n3 > n1 and n3 > n2 and n1 < n2:
    print(n3,n2,n1)
