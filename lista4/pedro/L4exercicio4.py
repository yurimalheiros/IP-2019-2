lista_vazia= list()
numero = int(input("Digite um número: "))  
while numero != 0:
  
  numero = int(input("Digite um número: "))
  if numero not in lista_vazia:
    lista_vazia.append(numero)
    
print(lista_vazia)