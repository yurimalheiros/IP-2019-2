a=float(input("Digite seu peso: "))
b=float(input("Digite sua altura: "))

imc=a/b**2

if imc>25:
    print("A pessoa está acima do peso.")
elif imc<18.5:
    print("A pessoa está abaixo do peso.")
else:
    print("A pessoa está com um peso normal.")
