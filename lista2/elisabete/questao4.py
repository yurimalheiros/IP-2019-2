x = int(input("digite um número"))
y = int(input("digite outro número"))
z = int(input("digite um último número"))
if a<b<c:
    print(a.b.c)
if a<c<b:
    print(a.c.b)
else:
    if b<a<c:
        print(b.a.c)
    if b<c<a:
        print(b.c.a)
if c<a<b:
    print(c.a.b)
if c<b<a:
    print(c.b.a)
elif a == b or a == c or b == c:
    print("Inválido")