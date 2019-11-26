peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso/(altura*altura)

if (imc < 18.5):
    print("Com", imc, "de IMC, você está abaixo do peso")

elif (imc > 25.0):
    print("Com", imc, "de IMC, você está acima do peso")

else:
    print("Com IMC de", imc,"você está com peso normal.")

