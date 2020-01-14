n = int(input("digite um numero"))
primo = true
i = 2
while i < n and primo:
    if n % i == 0:
         primo = false
    i += 1

if primo:
    print ("este é um numero primo")
else:
    print ("este não é um numero primo")