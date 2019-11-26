month = int(input('Digite o mes: '))
year = int(input('Quantos dias do ano: '))

if month == 1:
    print('O mes de Janeiro tem 31 dias')
if month == 2 and year % 365 == 1:
    print('O mes de Fevereiro tem 29 dias')
else:
    print('O mes de Fevereiro tem 28 dias')
if month == 3:
    print('O mes de Março tem 31 dias')
if month == 4:
    print('O mes de Abril tem 30 dias')
if month == 5:
    print('O mes de Maio tem 31 dias')
if month == 6:
    print('O mes de Junho tem 30 dias')
if month == 7:
    print('O mes de Julho tem 31 dias')
if month == 8:
    print('O mes de Agosto tem 30 dias')
if month == 9:
    print('O mes de Setembro tem 31 dias')
if month == 10:
    print('O mes de Outubro tem 30 dias')
if month == 11:
    print('O mes de Novembro tem 31 dias')
if month == 12:
    print('O mes de Dezembro tem 30 dias')

