n1= int(input ("digite um numero"))
n2= int(input ("digite um numero"))
n3= int(input ("digite um numero"))

if n2> n1 and n1>n3:
       print ("a ordem dos números são:{},{} e {}".format(n3,n1,n2))
       primeiro=n3
       segundo=n1
       terceiro=n2
if n2>n1 and n3>n2:
       print (("a ordem dos números são:{},{} e {}".format(n1,n2,n3)))
       primeiro=n1
       segundo=n2
       terceiro=n3
if n1>n3 and n3>n2:
       print ("a ordem dos números são:{},{} e {}".format(n2,n3,n1))
       primeiro=n2
       segundo=n3
       terceiro=n1
if n2>n3 and n1>n2:
       print("a ordem dos números são:{},{} e {}".format(n3,n2,n1))
       primeiro=n3
       segundo=n2
       terceiro=n1
if n3>n1 and n2>n3:
       print ("a ordem dos números são:{},{} e {}".format(n1,n3,n2))
       primeiro=n1
       segundo=n3
       terceiro=n2
if n1>n2 and n3>n1:
       print ("a ordem dos números são:{},{} e {}".format(n2,n1,n3))
       primeiro=n2
       segundo=n1
       terceiro=n3

