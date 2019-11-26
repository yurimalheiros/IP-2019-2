peso = float(input("seu peso"))
altura = float(input("sua altura"))
IMC = peso / altura ** 2
if(IMC > 18.5):
    print("está abaixo do peso)
elif(IMC < 20):
    print("esta acima do peso")
else:
