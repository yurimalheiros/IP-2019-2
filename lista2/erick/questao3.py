'''

2) Escreva um programa que recebe um ano como entrada e verifica se esse ano
é bissexto.

3) Escreva um programa que recebe um mês e um ano e exibe quantos dias tem
esse mês nesse ano. Use o código da questão anterior para ajustar os dias de
fevereiro.

'''

'''

Para ser bissexto, o ano deve ser:

- Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

- Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;

- Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, 
deixando o resto igual a zero.

'''

'''

Se for bissexto -> fevereiro têm 29 dias
Se não for bissexto -> fevereiro têm 28 dias

'''

mes = input("digite um mês no formato (01) -> Janeiro: ")
ano = int(input("ano: "))

if mes == "01":
  print("O mês de Janeiro têm 31 dias")
elif mes == "03":
  print("O mês de Março têm 31 dias")
elif mes == "04":
  print("O mês de Abril têm 30 dias")
elif mes == "05":
  print("O mês de Maio têm 31 dias")
elif mes == "06":
  print("O mês de Junho têm 30 dias")
elif mes == "07":
  print("O mês de Julho têm 31 dias")
elif mes == "08":
  print("O mês de Agosto têm 31 dias")
elif mes == "09":
  print("O mês de Setembro têm 30 dias")
elif mes == "10":
  print("O mês de Outubro têm 31 dias")
elif mes == "11":
  print("O mês de Novembro têm 30 dias")
elif mes == "12":
  print("O mês de Dezembro têm 31 dias")

elif (ano % 4 == 0 and ano % 400 != 0 and mes == "02"):
  print("O mês de Fevereiro têm 29 dias")
else:
  print("O mês de Fevereiro têm 28 dias")