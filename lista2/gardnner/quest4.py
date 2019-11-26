x=int(input("Entre com um numero: "))
y=int(input("Entre com mais um numero: "))
z=int(input("Entre com mais outro numero: "))
if (x>y)&(x>z):
    if y>z:
      print (x)
      print (y)
      print (z)
    else:
      print (x)
      print (y)
      print (z)
if (y>x)&(y>z):
    if x>z:
      print (y)
      print (x)
      print (z)
    else:
      print (y)
      print (z)
      print (x)
if (z>x)&(z>y):
    if x>y:
      print (z)
      print (x)
      print (y)
    else:
      print (z)
      print (y)
      print (x)