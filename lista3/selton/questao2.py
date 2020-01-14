n = int(input("Digite o valor de n: "))
fat = 1
mult = 2
while mult <= n:
    fat = fat * mult
    mult = mult + 1

print("O valor de",n ,"fatorial é:", fat)
