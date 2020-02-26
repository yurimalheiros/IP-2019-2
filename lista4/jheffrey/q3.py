lisnum = []
v = 0

while v == 0:
    print ("Digite 0 para parar")
    L = int(input('Insira os dados a ser acresentados a lista:'))
    lisnum.append(L)
    if L == 0:
        
        lisnum.pop(0)
        print(lisnum)
        print ("O dado de menor valor encontrado foi", lisnum[0])
        fim = lisnum[-1]
        print("o dado de maior valor encontrado foi", fim)