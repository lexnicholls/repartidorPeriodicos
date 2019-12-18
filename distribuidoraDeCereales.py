from sympy import Integral, integrate
from sympy.abc import x

#Compra - 20 * kilo
#Vende - 45 * kilo
#--------------------------------
#Demanda superior - 40 * kilo
#Excedente de arroz - 15 * kilo
#--------------------------------
#Ganancia con demanda superior - 5 * kilo
#Perdida por excedente de arroz - 5 * kilo
#--------------------------------
#Limite inferior - 72.8 kilos
#Limite superior - 149.8 kilos

compra = int(input("Ingrese el precio de compra: ")) 
venta =  int(input("Ingrese el precio de venta: ")) 
demanda =  int(input("Ingrese el precio de demanda: "))
excedente = int(input("Ingrese el precio del excedente: "))

limInferior =  int(input("Ingrese el limite inferior: "))
limSuperior =  int(input("Ingrese el limite superior: "))

ganancia = venta - compra
gananciaDemanda = venta - demanda
perdida = excedente - compra

fD = 1/(limSuperior-limInferior)




#if demanda >= 

print(ganancia,gananciaDemanda,perdida)