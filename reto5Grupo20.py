import pandas as pd

rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true' 
 
def listaPeliculas(rutaFileCsv: str) -> str: 
    temporal = rutaFileCsv.split('.')
    if 'csv' in temporal[-1]:
        try:
            df1 = pd.read_csv(rutaFileCsv)
            SubDf1 = df1[['Country','Language','Gross Earnings']]
            ganancias = SubDf1.pivot_table(index=['Country','Language'])
            return ganancias.head(10)
            
        except:
            return f'Error al leer el archivo de datos.'
            
    else:
        return'Extensión inválida.'
    
    
print(listaPeliculas(rutaFileCsv))