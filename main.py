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
columnaPagos = []

print("Ingrese los valores de la matriz:")

#t = []


for i in range(F):		 # A for loop for row entries
    celdaPeriodico = []
    for j in range(C):	 # A for loop for column entries
        celdaPeriodico.append(int(input()))
    matrizPeriodico.append(celdaPeriodico)

for i in range(len(matrizPeriodico)):
    columnaPagos.append(matrizPeriodico[i][1])

celdaPagos = [[]]



for i in range(len(columnaPagos)):
    celdaPagos.append([])
    for j in range(len(columnaPagos)):
        if columnaPagos[i] == columnaPagos[j] or columnaPagos[j] >= columnaPagos[i]:
            celdaPagos[j].append(columnaPagos[i]*ganancia)
        if columnaPagos[i] < columnaPagos[j]:
            celdaPagos[j].append((columnaPagos[j]*ganancia)-(columnaPagos[j]-columnaPagos[i]))
    matrizPagos.append(celdaPagos)

# For printing the matrix
print("Matriz periodico")
for i in range(F):
    for j in range(C):
        print(matrizPeriodico[i][j], end=" ")
    print()
print()


print("Columna pago")
for i in range(len(columnaPagos)):
        print(columnaPagos[i], end=" ")
print()

print("Matriz pago")
for i in range(F):
    for j in range(C):
        print(matrizPagos[i][j], end=" ")
    print()