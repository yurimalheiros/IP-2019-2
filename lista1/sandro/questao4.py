print("O horário atual é: 14 horas")
hora_atual = 14

tempo = input("Digite após quantas horas irá alarmar: ")

alarme = int(tempo) + hora_atual

print("Que horas o alarme irá tocar: ", alarme % 24, "horas")

