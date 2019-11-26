peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
altura_2 = altura * altura
imc = peso/altura_2

if imc <= 18.5:
    print("Você esta abaixo do peso com um IMC de:", imc)
elif imc >= 25:
    print("Você esta acima do peso comum IMC de:", imc)
else:
    print("Seu peso esta normal com IMC de:", imc)