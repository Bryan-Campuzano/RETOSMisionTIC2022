""" Resolución del reto 1
"""

""" esta funcion calcula el valor de las ganancias o perdidas de un CDT dependiendo de los valores dados

    Parámetros: usuario (str): alfanumérico que identifica el usurario 
            capital (int): Monto a ingresar 
            tiempo (int): Tiempo del CDT
    retorna:    String: de la forma "Las ganancias obtenidas para un monto de {}. en un tiempo de {} meses es {}"
"""
#   código que entra en la prueba
def CDT(usuario: str, capital: int, tiempo: int):
    porcentajeInterés = 0
    valorIntereses = 0
    valorTotal = 0
    if tiempo > 2:
        porcentajeInterés = 0.03
        valorIntereses = (capital * porcentajeInterés * tiempo)/12 
        valorTotal = capital + valorIntereses
    else:
        porcentajeInterés = 0.02
        valorIntereses = capital * porcentajeInterés
        valorTotal = capital - valorIntereses
    return ("Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}".format(usuario,capital,tiempo,valorTotal))        

#   Banco de pruebas  
print(CDT("AB1012",1000000,3)) 
print(CDT("ER3366",650000,2))

# appEnd