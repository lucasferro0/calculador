import math
import os
# CALCULANDO RAÍZES
def calcular(a,b,c):
    delta = (b**2)-(4*a*c)
    if delta < 0:
        return "Não há raiz real"
    elif delta == 0:
        raizdelta = math.sqrt(delta)
        x1 = (-b + raizdelta)/2*a
        x2 = (-b - raizdelta)/2*a
        return (x1,x2)
    else:
        raizdelta = math.sqrt(delta)
        x1 = (-b + raizdelta)/2*a
        x2 = (-b - raizdelta)/2*a
        return (x1, x2)
# RECEBER VALORES DE A, B, C (aX2+bX+c)
listaA=[]
listaB=[]
listaC=[]
quantidade = int(input("Digite a quantidade de equações: "))
os.system("cls")
cont = 1
while cont <= quantidade:
    print(f"\nDigite os valores da equação {cont}")
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    listaA.append(a)
    listaB.append(b)
    listaC.append(c)
    cont+=1
os.system("cls")
# MOSTRANDO RAÍZES
cont2 = 0
for e in listaA:
    raizes = calcular(e,listaB[cont2],listaC[cont2])
    if raizes == "Não há raiz real":
        print(f"Equação {cont2+1}:\nNão há raízes reais.\n")
    else:
        print(f"Equação {cont2+1}:\nx1 = {raizes[0]}\nx2 = {raizes[1]}\n")
    cont2+=1
