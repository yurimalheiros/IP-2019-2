v1 = int(input("Digite um numero: "))
v2 = int(input("Digite um numero: "))
v3 = int(input("Digite um numero: "))

if v1 > v2 > v3:
    print(v1, v2, v3)
elif v1 > v3 > v2:
    print(v1, v3, v2)
elif v3 > v2 > v1:
    print(v3, v2, v1)
elif v3 > v1 > v2:
    print(v3, v1 ,v2)
elif v2 > v3 > v1:
    print(v2, v3, v1)
elif v2 > v1 > v3:
    print(v2, v1, v3)