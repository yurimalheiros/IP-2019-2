peso= float(input("Digite seu peso: "))
altura= float(input("Digite sua altura: "))
imc = peso / (altura**2)

if  imc < 18.5:
    print("Seu Imc é: ",imc)
    print("Você esta a baixo do peso! ")
    
elif imc > 25:
    print("Seu Imc é: ",imc)
    print("Você esta acima do peso! ")

if imc <= 25 and imc >= 18.5 :
    print("Seu Imc é: ",imc)
    print("Seu peso esta normal ")
