peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura**2)
print("seu imc é:", imc)
if imc < 18.5:
  print("abaixo do peso")
elif 18 <= imc < 25:
  print("peso ideal")
