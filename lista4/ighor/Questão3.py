N = int(input("Digite um número"))
lista = []

MaiorValor = N
MenorValor = 0

while N != 0:
    lista.append(N)
    if N  > MaiorValor:
        MaiorValor = N
    elif N < MenorValor:
        MenorValor = N

    N = int(input("Digite outro número"))

print(lista)
print(MaiorValor , MenorValor)
        
