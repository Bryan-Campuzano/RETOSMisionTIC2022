""" Resolución del reto 3

    realizar un programa que cree un registro de ventas de autopartes, la informacion de la venta esta dada
    como una lista de tuplas que contiene los datos de la venta y retorna un diccionario con el registro de las ventas
    hechas
    
    el programa debe permitir cargar datos al diccionario, debe mostrar 
    un listado completo del diccionario y debe permitir consultar un producto 
    por su llave
"""
#--------------------DECLARACIÓN DE LISTAS---------------------
ventas1 = [ 
    (2001,'rosca' , 'PT29872',2,45 , 'Luis Molero'  ,3456,'12/06/2020'), 
    (2010,'bujía' , 'MS9512' ,4,15 , 'Carlos Rondon',1256,'12/06/2020'), 
    (2010,'bujía' , 'ER6523' ,9,36 , 'Pedro Montes' ,1243,'12/06/2020'),     
    (3578,'tijera', 'QW8523' ,1,128, 'Pedro Faria'  ,1456,'12/06/2020'), 
    (9251,'piñón' , 'EN5698' ,2,8  , ' Juan Peña'   ,565 ,'12/06/2020')]
ventas2 = [ 
    (5489,'tornillo', 'RS8512',2,33 ,'Julio Perez' ,3654213 ,'13/06/2020'), 
    (3215,'zocalo'  , 'UM8587',2,125,'Laura Macias',1256321 ,'13/06/2020'), 
    (3698,'biela'   , 'PT3218',1,78 ,'Luis Peña'   ,14565487,'13/06/2020'), 
    (8795,'cilindro', 'AZ8794',2,96 ,'Carlos Casio',5612405 ,'13/06/2020')]
ventas3 = [ 
    (9852,'Culata' , 'XC9875' ,2,165,'Luis Molero' ,3455846,'14/06/2020'), 
    (9852,'Culata' , 'XC9875' ,2,165,'Jose Mejia'  ,1355846,'14/06/2020'), 
    (2564,'Cárter' , 'PT29872',2,32 ,'Peter Cerezo',8545436,'14/06/2020'), 
    (5412,'válvula', 'AZ8798' ,2,11 ,'Juan Peña'   ,568975 ,'14/06/2020')]

#------------------------ZONA DE CÓDIGO 1------------------------
#------------------------SOLUCIÓN 1 (NOTA OBTENIDA: 4,17)------------------------
""" este método toma una lista de tuplas referente al registro de cada venta realizada y genera un diccionario
    con todas estas ventas indexadas 
        parámetros: ventas(List): lista que contiene las tuplas con la informacion de cada venta realizada
        
        retorna: diccionarioTemp(dict): diccionario con los datos de las ventas, indexado con llaves para su organización
"""
def AutoPartes(ventas: list):
    diccionarioTemp = {}
    for i in range(0,len(ventas)):
        diccionarioTemp.setdefault(i,ventas[i])
    return diccionarioTemp
    
""" este método recibe como parámetro una lista, la cual es pasada por el método AutoPartes() para su indexacion
    ademas de un entero idProducto, numero de identificación único por pieza y retorna todas las ventas realizadas
    de este producto, mensaje de error de no encontrar ninguna venta realizada bajo este id de producto
        parámetros: ventas(dict): lista que contiene las tuplas con la informacion de cada venta realizada
                    idProducto(int): numero de identificación único por pieza
        retorna:    temp(str): string de la forma 
                    'Producto consultado : IdProducto Descripción dProducto #Parte pnProducto Cantidad vendida cvProducto Stock sProducto Comprador nComprador Documento cComprador Fecha Venta fVenta' 
                    de encontrar ventas bajo el id proporcionado, o un string de la forma 
                    'No hay registro de venta de ese producto'
                    cuando no encuentra ventas bajo el id proporcionado
"""
def consultaRegistro(ventas, idProducto): 
    temp = ""
    cantidadRetorno = 0
    for i in range(0,len(ventas)):
            venta = (ventas[i])
            if (venta[0] == idProducto): 
                temp = f"Producto consultado : {venta[0]}  Descripción  {venta[1]}  #Parte  {venta[2]}  Cantidad vendida  {venta[3]}  Stock  {venta[4]}  Comprador {venta[5]}  Documento  {venta[6]}  Fecha Venta  {venta[7]}"
                print(temp)
            elif(cantidadRetorno == 0):
                cantidadRetorno += 1
            elif (temp =="" and cantidadRetorno != 0):
                temp = "No hay registro de venta de ese producto" 
                print(temp)
            else:
                pass    
           
#-------------------------ZONA DE TEST 1-------------------------
print("----------------separador-------------@------")
consultaRegistro(AutoPartes(ventas1),2010)
consultaRegistro(AutoPartes(ventas2),2001)
consultaRegistro(AutoPartes(ventas3),9852)
print("----------------separador--------------@-----")

#------------------------SOLUCIÓN 2 (NOTA: 5.0)------------------------
#------------------------ZONA DE CÓDIGO 2------------------------
""" este método toma una lista de tuplas referente al registro de cada venta realizada y genera un diccionario
    con todas estas ventas indexadas 
        parámetros: ventas(List): lista que contiene las tuplas con la informacion de cada venta realizada
        
        retorna: diccionarioTemp(dict): diccionario con los datos de las ventas, indexado con llaves para su organización
"""
def AutoPartes2(ventas: list):
#   el cambio mas importante entre la solución propuesta y mi solución anterior es que cada elemento en el 
#   diccionario es guardado como una lista cuya llave es el id del producto, teniendo pues una lista de 
#   tuplas, cada tupla con la informacion de la venta, haciendo pues que en cada id de producto
#   se guarden todos los registros de ventas, a diferencia del diccionario de AutoPartes, que almacenaba cada venta
#   individualmente
    diccionario = {}
    for i in ventas:
        if diccionario.get(i[0]) == None:
            diccionario[i[0]] = []
        diccionario[i[0]].append((i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    
    return diccionario

""" este método recibe como parámetro una lista, la cual es pasada por el método AutoPartes() para su indexacion
    ademas de un entero idProducto, numero de identificación único por pieza y retorna todas las ventas realizadas
    de este producto, mensaje de error de no encontrar ninguna venta realizada bajo este id de producto
        parámetros: ventas(List): lista que contiene las tuplas con la informacion de cada venta realizada
                    idProducto(int): numero de identificación único por pieza
        retorna:    temp(str): string de la forma 
                    'Producto consultado : IdProducto Descripción dProducto #Parte pnProducto Cantidad vendida cvProducto Stock sProducto Comprador nComprador Documento cComprador Fecha Venta fVenta' 
                    de encontrar ventas bajo el id proporcionado, o un string de la forma 
                    'No hay registro de venta de ese producto'
                    cuando no encuentra ventas bajo el id proporcionado
"""
def consultaRegistro2(ventas, idProducto):
#   en este caso no falla en el recorrido del diccionario como el original, pues, Autopartes fallaba pues no permitía hacer todas esas iteraciones
#   de recorrido, pues hacer 2600 recorridos mínimo por cada elemento resultaba muy pesado, por eso se opto por no hacerlo de esta manera en la primera
#   solución, por esto se almacenaba cada venta por aparte con un entero estándar comenzando desde cero
#   pero eso se soluciona almacenando todas las ventas en un mismo idProducto gracias a una lista de tuplas hecha en Autopartes2
#   y para retornar todas las ventas de cada producto, unicamente recorremos los elementos de la lista obtenida 
    if idProducto in ventas:
        for i in (ventas[idProducto]):
            print(f"Producto consultado : {idProducto}  Descripción  {i[0]}  #Parte  {i[1]}  Cantidad vendida  {i[2]}  Stock  {i[3]}  Comprador {i[4]}  Documento  {i[5]}  Fecha Venta  {i[6]}")
    else:
        print('No hay registro de venta de ese producto')

#-------------------------ZONA DE TEST 2-------------------------
print("----------------separador-------------@------")
consultaRegistro2(AutoPartes2(ventas1),2010)
consultaRegistro2(AutoPartes2(ventas2),2001)
consultaRegistro2(AutoPartes2(ventas3),9852)
print("----------------separador--------------@-----")

#   appEnd