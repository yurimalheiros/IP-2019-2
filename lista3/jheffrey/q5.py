op = input ("Digite a operacao (res1 para: + e -, res2 para: * e / ) ")
a = int(input("Tecle '1' para mostrar a tabuada do 9 "))
contador = 9
res1 = a + contador
res2 = a - contador

for res1 in range (1, 2):
    if op == "res1":
        print ("+ \n9+1=10 \n9+2=11 \n9+3=12 \n9+4=13 \n9+5=14 \n9+6=15 \n9+7=16 \n9+8=17 \n9+9=18 \n- \n9-1=8 \n9-2=7 \n9-3=6 \n9-4=5 \n9-5=4 \n9-6=3 \n9-7=2 \n9-8=1 \n9-9=0")

    if op == "res2":
        print ("* \n9*1=9 \n9*2=18 \n9*3=27 \n9*4=36 \n9*5=45 \n9*6=54 \n9*7=63 \n9*8=72 \n9*9=81 \n/ \n9/9=1 \n18/9=2 \n27/9=3 \n36/9=4 \n45/9=5 \n54/9=6 \n63/9=7 \n72/9=8 \n81/9=9")
