ano = int(input("seu ano"))
if(ano % 100 != 0) and (ano % 4 == 0 or ano % 400 == 0):
    print("É um ano bissexto")
else:
    print("não é ano bissexto")
