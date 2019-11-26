x=int(input("Digite o primeiro número: "))
y=int(input("Digite o segundo número: "))
z=int(input("Digite o terceiro número: "))
if x > y > z:
    print(x,y,z)
if x > z > y:
    print(x,z,y)
if y > x > z:
    print(y,x,z)
if y > z > x:
    print(y,z,x)
if z > x > y:
    print(z,x,y)
if z > y > x:
    print(z,y,x)
if x == y or x == z or y == z:
    print("Número inválido")
