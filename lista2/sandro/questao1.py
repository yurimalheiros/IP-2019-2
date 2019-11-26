peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é sua altura? " ))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso normal") 
else:
    if imc > 25.0:
        print("Você está acima do peso normal")
    else: 
        print("Seu peso está normal")
