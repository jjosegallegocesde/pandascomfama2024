#1. Importar el paquete o paquetes con los que voy
#a analizar la informacion
import pandas as pd

def analizarCanastaBasica():
    #2. Sin importar la fuente (sql, xls, JSON, csv...)
    #crear una tabla tabulada que se lama DATAFRAME
    tabla=pd.read_csv('./data/bdcanasta.csv')
    #print(tabla)

    #3. Aplico filtros para limpiar o seleccionar datos

    #print(tabla.head(20)) #primeros N registros
    #print(tabla.tail())

    print(tabla.describe())

