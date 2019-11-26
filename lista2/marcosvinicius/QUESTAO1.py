
peso =  float (input('digite seu peso:KG'))
altura =float (input('digite sua altura:METROS'))
imc = peso/altura**2
print('o seu IMC é {:.1f}:'.format(imc))
if imc <=18.5:
    print('você está abaixo do peso')
elif imc>25:
    print('você está acima do peso')
else: print('Você está no peso adequado,Parabéns!')
