alarme = 14
pedido_alarme = 51

result_alarme = alarme + (pedido_alarme % 24)

print('O seu alarme irá tocar de {}h'.format(result_alarme))
