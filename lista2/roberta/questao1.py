# Função: Calcular peso com o IMC
# Autor: Roberta de Lima Ribeiro

print("CALCULAR PESO")

peso = int(input("Digite peso"))
altura = float(input("Digite a altura"))
imc = peso/(altura**2)

print("Seu IMC: ", imc)
if (imc<18.5):
    print("Abaixo do peso")
elif (imc>25):
    print("Acima do peso")
else :
    print("Peso normal")

print("fim do programa")
