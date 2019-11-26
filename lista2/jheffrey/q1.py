print ("questao 1")

a = float(input("Digite a altura:CM"))
b = float(input("Digite o peso "))
imc = b/a**2
print ("seu imc é:",imc)
if imc <= 18.5:
    print ("abaixo do peso")
elif imc >25: 
    print ("acima do peso ")
else : 
    print ("peso ideal")
