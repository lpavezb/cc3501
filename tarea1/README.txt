INSTRUCCIONES DE EJECUCION TAREA 1

Para ejecutar la tarea se debe modificar la función main ubicada en la linea 396.

Primero se debe crear el objeto Tarea(ancho=2000, largo=4000, dh=0.08, factor=0.005), se puede crear sin darle
parametros, o darle parametros de largo y anchode la matriz, el dh a utilizar y
el factor para reducir el tamaño de la matriz.

Despues se puede llamar al metodo doTarea(hora=0, rho=False), que recive la hora (0 - 24) y un valor bool que dice
si se ocupa la funcion rho (True), o si se usa rho=0 (False).
Este metodo inicializa la geografia y condiciones de borde, luego realiza las iteraciones y plotea el grafico de
temperaturas.

Si se quiere probar con distintos valores para w con un numero fijo de 1000 iteraciones, se puede llamar al metodo
doTarea2(w_r=1.96), que recibe el w que se quiere probar, este metodo retorna el tiempo en el que se demora en realizar
las 1000 iteraciones.