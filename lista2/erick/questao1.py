'''
1) O Índice de Massa Corporal (IMC) é uma medida que avalia o peso ideal de
uma pessoa. Ele é calculado pela fórmula:
IMC =
peso
altura2
Um IMC menor que 18,5 indica que a pessoa está abaixo do peso. Um IMC
maior que 25 indica que a pessoa está acima do peso. Um IMC entre esses dois
valores indica um peso normal.
Escreva um programa que recebe o peso e a altura do usuário e exibe se ele está
abaixo do peso, acima do peso ou com o peso normal de acordo com o IMC.
'''

peso = float(input("Digite o peso: "))
altura = float(input("Digite a alutura: "))
IMC = peso / (altura ** 2)

if (IMC < 18.5):
    print("Seu IMC é: %.2f"% IMC, " Você é considerado abaixo do peso")
elif (IMC > 25):
    print("Seu IMC é: %.2f"% IMC, " Você é considerado acima do peso")
elif (IMC > 18.5 and IMC < 25):
    print("Seu IMC é: %.2f"% IMC, " Seu peso é considerado normal")
    
                  
