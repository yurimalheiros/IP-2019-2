a=int(input("Digite o primeiro número: "))
b=int(input("Digite o segundo número: "))
c=int(input("Digite o terceiro número: "))

if a<b<c:
    print(a, b, c)
if a<c<b:
    print(a,c,b)
else:
    if b<a<c:
        print(b,a,c)
    if b<c<a:
        print(b,c,a)
if c<a<b:
    print(c,a,b)
elif c<b<a:
   print(c,b,a)

else:
    if a==b or a==c or b==c:
        print("Não é válido.")
