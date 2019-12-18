import numpy

compra = 5
venta = 8
remate = 4
ganancia = 3

F = 5  # Filas
C = 2  # Columnas

#t1 = 'No. Dias'
#t2 = 'Demanda'

matrizPeriodico = []
matrizPagos = []
columnaDias = []
columnaDemandas = []

print("Ingrese los valores de la matriz:")

#t = []

#Declarar matriz
for i in range(F):		 # Ciclo para las filas en la matriz
    celdaPeriodico = []
    for j in range(C):	 # Ciclo para las columnas en la matriz
        celdaPeriodico.append(int(input()))
    matrizPeriodico.append(celdaPeriodico)

#Extraer columna 1
for i in range(len(matrizPeriodico)):
    columnaDias.append(matrizPeriodico[i][0]/100)

#Extraer columna 2
for i in range(len(matrizPeriodico)):
    columnaDemandas.append(matrizPeriodico[i][1])

#Crear matriz de pagos
for i in range(len(columnaDemandas)):
    for j in range(len(columnaDemandas)):
        matrizPagos.append(columnaDemandas)

#Multiplicar la matriz de pago por un escalar
matrizPagos = ganancia * numpy.array(matrizPagos)
matrizPagosT = matrizPagos.transpose()

matrizCopia = matrizPagosT

#Procesar matriz para EMV
for i in range(len(columnaDemandas)):
    for j in range(len(columnaDemandas)):  
        if columnaDemandas[i] > columnaDemandas[j]:
            matrizPagosT[i][j] = matrizCopia[j][i]-(columnaDemandas[i]-columnaDemandas[j]) 

#EMV
#for i in range(len(columnaDemandas)):
columnaEMV = []
sum = 0
res = 0
for i in range(len(columnaDias)):
    for j in range(len(columnaDias)):
        sum = matrizPagosT[i][j]*columnaDias[j]
        res +=sum
    columnaEMV.append(res)
    sum=0
    res=0

#Imprimir matrices
print("Matriz periodico")
for i in range(F):
    for j in range(C):
        print(matrizPeriodico[i][j], end=" ")
    print()
print()


print("Columna Dias")
for i in range(len(columnaDias)):
        print(columnaDias[i], end=" ")
print()
print()

print("Columna Demandas")
for i in range(len(columnaDemandas)):
        print(columnaDemandas[i], end=" ")
print()
print()

print("Matriz pago")
for i in range(F):
    for j in range(len(columnaDemandas)):
        print(matrizPagosT[i][j], end=" ")
    print()
print()
print()



print("EMV")
for i in range(len(columnaEMV)):
        print(columnaEMV[i], end=" ")
print()
print()

#