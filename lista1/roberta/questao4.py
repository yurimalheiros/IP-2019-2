# Função Definir alarme
# Autor Roberta de Lima

from datetime import datetime, timedelta

# Função Estática
print("ALARME")
dt = datetime(2019,11,3, 14)
hrAlarme = dt +  timedelta(hours=51)
print("Sendo 14hrs, daqui a 51hrs o alarme tocará às ",hrAlarme.strftime("%H:%M "))


# Função dinâmica
#tempo = int(input("Digite o tempo para alarme(horas): "))
#hj = datetime.now()
#hrAlarme = hj + timedelta(hours=tempo)
#print("Hora do alarme: ", hrAlarme.strftime("%H:%M %d/%m/%Y"))

