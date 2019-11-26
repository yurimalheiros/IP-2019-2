print ("Questão 1")
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = (peso/altura**2)

if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc >= 18.5 and imc < 25:
    print("Você está com o peso normal!")
elif imc > 25:
    print("Você está acima do peso!")
else:
    print("verifique os dados!")

