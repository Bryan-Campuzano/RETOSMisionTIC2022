"""Resolución del reto 2
"""
#------------------------ZONA DE CÓDIGO------------------------

""" esta función recibe una informacion de cliente dada en forma de diccionario y retorna un diccionario con 
    una nueva variedad de datos, como el nuevo costo de boleta, si es o no apto para ingreso
    
    Parámetros: informacion (dict): diccionario con el listado de parámetros con la forma: [id_client,nombre,edad,primer_ingreso]              
    retorna:    nuevoDiccionario (Dict): diccionario con el listados de productos de la forma: [nombre,edad,atraccion,apto,primer_ingreso,total_boleta]
"""
def cliente(informacion:dict)->dict:
    
    if informacion['edad'] > 18:
        atraccionV = 'X-Treme'
        aptoV = True
        if informacion['primer_ingreso'] == True:
            total_boletaV = 20000 - ((20000) * 0.05)
        else:
            total_boletaV = 20000
    elif informacion['edad']>=15 and informacion['edad']<=18:
        atraccionV = 'Carros chocones'
        aptoV = True
        if informacion['primer_ingreso'] == True:
            total_boletaV = 5000 - ((5000) * 0.07)
        else:
            total_boletaV = 5000
    elif informacion['edad']>=7 and informacion['edad']<15:
        atraccionV = 'Sillas voladoras'
        aptoV = True
        if informacion['primer_ingreso'] == True:
            total_boletaV = 10000 - ((10000) * 0.05)
        else:
            total_boletaV = 10000
    else:
        atraccionV = 'N/A'
        aptoV = False
        total_boletaV = 'N/A'
    
    nuevoDiccionario ={
        'nombre':informacion['nombre'],
        'edad':informacion['edad'],
        'atraccion': atraccionV,
        'apto':aptoV,
        'primer_ingreso':informacion['primer_ingreso'],
        'total_boleta': total_boletaV
    }
    return nuevoDiccionario

#-------------------------ZONA DE TEST-------------------------

info1 ={
    'id_cliente': 1,
    'nombre': 'Johanna Fernandez', 
    'edad': 20, 
    'primer_ingreso': True
}
info2 ={
    'id_cliente': 1,
    'nombre': 'Johanna Fernandez', 
    'edad': 20, 
    'primer_ingreso': False
}
info3 ={
    'id_cliente': 2,
    'nombre': 'Gloria Suarez', 
    'edad': 3, 
    'primer_ingreso': True
}
info4 ={
    'id_cliente': 3,
    'nombre': 'Tatiana Suarez', 
    'edad': 17, 
    'primer_ingreso': True
}
info5 ={
    'id_cliente': 3,
    'nombre': 'Tatiana Suarez', 
    'edad': 17, 
    'primer_ingreso': False
}
info6 ={
    'id_cliente': 4,
    'nombre': 'Tatiana Ruiz', 
    'edad': 8, 
    'primer_ingreso': True
}
info7 ={
    'id_cliente': 4,
    'nombre': 'Tatiana Ruiz', 
    'edad': 8, 
    'primer_ingreso': False
}

print(cliente(info1))
print(cliente(info2))
print(cliente(info3))
print(cliente(info4))
print(cliente(info5))
print(cliente(info6))
print(cliente(info7))

#   appEnd