docente=1
estudiante=2
Productos=[]

doc=eval(input("ingrese su número de documento: "))
rol=eval(input("ingrese si es docente o estudiante: "))

CantProd=eval(input("ingrese cuantos productos va a llevar: "))
CompraTotal=0

for x in range(CantProd):
    cod=str((input("ingrese el codigo del producto: ")))
    PrecioCompra=eval(input("ingrese el precio por unidad de producto: "))
    cant=eval(input("ingrese cuantas unidades del producto va a llevar: "))
    PrecioTotal=PrecioCompra*cant
    CompraTotal+=PrecioTotal
    Productos.append(cod)

Total=0

if rol == docente or rol == 1:
    Total=CompraTotal*0.8
elif rol == estudiante or rol == 2:
    Total=CompraTotal*0.5

print("El " +str(rol) + " con cedula " + str(doc) + " debe pagar " + str(Total) + " por los productos " + str(Productos))