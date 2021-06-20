# ParcialHerramientasComputacionales
El objetivo de este programa es  aplicar descuentos en la cafeteria de la  universidad dependiendo del rol  (si es estudiante o docente)
primero que todo  empezamos creando las variables de estudiante y docente que vamos a utilizar mas a delante en la variable rol;
creamos una lista vacia llamada productos donde vamos a guardar los codigos de los productos que compran los clientes;
primeramente se pide por medio de la varibale doc, que significa Documento, que ingrese el numero de identificaación
después utilizamos la la variable rol  que vamos a necesitar para aplicar el descuento (el problema con esta variable es que si no ingresa una de las variables establecidas anteriormente ya sea 
estudiante o docente, no va a  aplicar el descuento ; el segundo problema es que al momento de imprimir el resultado, la variable rol aparece como el número que se le asignó a la variable, ya sea 1 que es igual a docente o 2 que es igual a estudiante);
creamos la variable CantProd que significa cantidad de productos, esta variable la utilizamos para poder crear un ciclo que le permita al cliente llevar varios productos a la vez; 
después creamos la variable CompraTotal que va acumulando el precio total de cada producto y los va sumando;
creamos un ciclo con for que se repita las veces que el cliente dijo que iba a comprar en la variable CantProd, dentro de este ciclo creamos la variable cod que significa codigo que es donde se va a pedir el codigo del producto que pidió el cliente, luego creamos la variable PrecioCompra que es donde se pide el precio del producto que pidió anteriormente por unidad, después se crea la varibale cant que significa cantidad y en esta variable se pide que ingrese cuantas unidaddes va a llevar del producto; dentro del mismo ciclo creamos la variable PrecioTotal que es donde se va a guardar la multiplicacion entre precio por unidad del producto y la cantidad de unidades del producto que va a llevar (ej: 1200 * 3; donde 1200 es el precio por unidad del producto y 3 es la cantidad que va a llevar de ese producto);
el resultado de la operación anterior se agrega a la variable creada anteriormente llamada PrecioTotal y ese resultado se envia a la variable CompraTotal que es donde se suma con las otras compras;
al final del ciclo utlizamos .append sobre la lista creada llamada productos para agregar el código del producto que se compro a dicha lista; 
salimos del ciclo y creamos la variable Total que es donde se va a almacenar el precio final a pagar con el descuento incluido
creamos un condicional donde si el rol es igual a docente o es igual a 1 (la variable docente le asignamos el valor 1 como lo dijimos anteriormente) entonces a la CompraTotal le quitamos el 20%
si el rol es igual a estudiante o es igual a 2 entonces a la CompraTotal le quitamos el 50%
salimos de este condicional e imprimimos el rol, la cedula del cliente, el total a pagar(con su descuento respectivo) y los productos que compró y por los cuales debe pagar
