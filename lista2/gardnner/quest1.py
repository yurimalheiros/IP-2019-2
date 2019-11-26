ps= float(input("digite o peso"))
alt= float(input("digite a altura"))
Imc= ps/alt**2

If imc <= 18.5:
     print("esta pessoa está abaixo do peso")
elif imc >= 25:
     print("esta pessoa está acima do peso")
else imc >= 18.5 and imc <= 25:
      print("esta pessoa está com o peso normal")