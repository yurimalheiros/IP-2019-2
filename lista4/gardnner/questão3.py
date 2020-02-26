listaNum = [ ]
for i in range(0,5):
     listaNum.append(int(input(f'Digite o {i+1}º valor: '))) 
print('=-' * 30) 
print(f'Você digitou os valores {listaNum}') 
print(f'O maior número é o {max(listaNum)}, cuja posição é {listaNum.index(max(listaNum))}')
print(f'O menor número é o {min(listaNum)}, cuja posição é {listaNum.index(min(listaNum))}')