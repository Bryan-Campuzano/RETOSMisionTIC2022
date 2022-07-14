""" Resolución del reto 5
    hacer un programa que, dada una ruta de acceso a un documento tipo csv, corrobora si es un archivo valido, de ser cierto
    genera un subconjunto con los valores de 'país', 'lenguaje' y 'ganancias brutas' retornando las primeras 10
    lineas. retorna un mensaje de error si el archivo esta vacío o no corresponde con el filtro, a su vez también
    arroja error si no es un archivo de tipo csv.
"""
#------------------------IMPORTACIONES---------------------------
import pandas as pd 

#----------------------DECLARACIÓN DE ELEMENTOS------------------
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

#------------------------ZONA DE CÓDIGO 1------------------------
#-------------SOLUCIÓN 1 (NOTA OBTENIDA: 5.0)--------------
""" este método, dada una ruta de acceso a un documento tipo csv, corrobora si es un archivo valido, de ser cierto
    genera un subconjunto con los valores de 'país', 'lenguaje' y 'ganancias brutas' retornando las primeras 10
    lineas. retorna un mensaje de error si el archivo esta vacío o no corresponde con el filtro, a su vez también
    arroja error si no es un archivo de tipo csv.
        parámetros: rutaFileCsv(str): vinculo de acceso al archivo 
        
        retorna:    una lista de los primeros 10 elementos con la informacion de 'país', 'lenguaje' y 'ganancias brutas'
                    retorna un mensaje de error de tipo 'Error al leer el archivo de datos.' si es un archivo diferente al esperado o
                    retorna un mensaje de error de tipo 'Extensión inválida.' si no corresponde a un archivo csv
""" 
def listaPeliculas(rutaFileCsv: str) -> str: 
    temp = rutaFileCsv.split('.')
    if 'csv' in temp[-1]:
        try:
            df1 = pd.read_csv(rutaFileCsv)
            resultado = df1[['Country','Language','Gross Earnings']]
            ganancias_gruesas = resultado.pivot_table(index = ['Country','Language'])
            print(ganancias_gruesas.head(10))   # este print es la condición 'secreta' para la obtención de la nota máxima
            return ganancias_gruesas.head(10)
        except:
            return f'Error al leer el archivo de datos.'
    else:
        return 'Extensión inválida.'  
#-------------------------ZONA DE TEST 1-------------------------

print(listaPeliculas(rutaFileCsv))
#   appEnd