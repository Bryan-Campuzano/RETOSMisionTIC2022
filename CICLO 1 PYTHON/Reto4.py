""" Resolución del reto 4

    Un contador necesita llevar una bitácora acerca de los registros diarios de una papelería, para esto
    tiene que automatizar el proceso de entrada y salida de facturas en un codigo que le permita recibir 
    un registro de ordenes (lista de tuplas) y efectuar los siguientes procesos:
        • Sumar el total de cada tupla de cada lista 
        • Sumar los totales de todas las tuplas de toda la lista 
        • Suma  el  incremento  si  la  compra  no  llega  a  un  mínimo  de  600.000  pesos
          en  este  caso,  se incrementa 25.000 pesos al total de la compra. 
 
    Recuerde, que la salida no debe tener más de dos decimales.
"""
#------------------------IMPORTACIONES---------------------------
from functools import reduce
#----------------------DECLARACIÓN DE LISTAS---------------------
facturas1 = [
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],  
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)], 
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)], 
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390)]
]
facturas2 = [
    [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
    [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)]
]
facturas3 = [
    [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)], 
    [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)], 
    [6591, ("7812", 2, 11.99), ("9652",11,18.99)]
]
#------------------------ZONA DE CÓDIGO 1------------------------
#------------------------SOLUCIÓN 1 (NOTA OBTENIDA: 5.0)------------------------
""" este método recibe una rutina contable que no es mas que una serie de facturas almacenadas en listas con tuplas
    internas, donde cada tupla es un producto, los productos vendidos y su valor unitario y retorna un string con los 
    valores totales de cada factura
        parámetros: rutinaContable(list): lista que contiene las facturas en forma de lista de tuplas
        retorna: una cadena de la forma 'La factura <número> tiene un total en pesos de <cantidad>' por cada factura
"""
def ordenes(rutinaContable): 
    from functools import reduce    # este import solo se hace aquí para el envío del reto a la plataforma, no es necesario importar dos veces
    print('------------------------ Inicio Registro diario ---------------------------------') 
    # REQUERIMIENTO 1: Sumar el total de cada tupla de cada lista
    lisTemp = list(map(lambda x: [x[0]]+ list(map(lambda y: y[1]*y[2] ,x[1:])) ,rutinaContable))
    # REQUERIMIENTO 2: Sumar los totales de todas las tuplas de toda la lista
    lisTemp2 = list(map(lambda x: [x[0]]+ [reduce(lambda a,e: a+e,x[1:])],lisTemp))
    # REQUERIMIENTO 3: Suma  el  incremento  si  la  compra  no  llega  a  un  mínimo  de  600.000  pesos, en  este  caso,  se incrementa 25.000 pesos al total de la compra
    lisTemp3 = list(map(lambda x: x if x[1] >= 600000 else [x[0]]+[x[1]+25000],lisTemp2))
    # REQUERIMIENTO 4: Imprime un string por cada factura, cada valor debe tener máximo dos decimales
    for i in range(0,len(lisTemp3)):
        print(f'La factura {lisTemp3[i][0]} tiene un total en {lisTemp3[i][1]:,.2F}')
    print('-------------------------- Fin Registro diario ----------------------------------')

#-------------------------ZONA DE TEST 1-------------------------
ordenes(facturas1)
ordenes(facturas2)
ordenes(facturas3)

#   appEnd
