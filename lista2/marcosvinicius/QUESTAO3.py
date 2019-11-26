mes= int(input("digite um mes"))
ano = int(input("digite um ano"))
if mes==2 and ano %4 == 0 or 100!= 0 and 400 == 0:
    print("o mês  {} tem 29 dias".format(mes))
else:print ("o mês {} tem 28 dias".format(mes))
if (mes==1) or (mes==3) or (mes==5) or (mes==7) or (mes==8) or (mes==10) or (mes==12):
    print ('o mês {} tem 31 dias'.format(mes))
elif  (mes==4)or (mes==6) or (mes==9) or (mes==11):
    print ('o mês {} tem 30 dias'.format(mes))
if ano %4 == 0 or 100!= 0 and 400 == 0:
       print ("o {} é bissesto".format(ano))
else:
    print ("o ano {} nao é bissesto.".format(ano))
