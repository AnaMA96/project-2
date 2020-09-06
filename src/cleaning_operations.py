import numpy as np


def nullPer(df, columns):
    '''Esta función sirve para calcular el porcentaje 
    de datos nulos de las columnas'''
    for i in columns:
        null_rate = df[i].isna().sum() / len(df) * 100 
        if null_rate > 0 :
            print(f"{i} has a {null_rate}% of null rate")

def stripObject(df, columns):
    '''Función para quitar los espacios antes y después
    de los valores de las columnas'''
    for column in columns:
        if df[column].dtype == np.object:
            df[column] = df[column].str.strip()
    return df

 
from time import strptime
import datetime

def dateConvert(month):
    '''Esta función transforma los meses por nombre en meses 
    por número. La excepción captura el error que devuelven los
    de datos nulos de las columnas'''
    try:
        datetime_object = strptime(month, "%B").tm_mon
    except:
        return month
    return datetime_object
    

def month_extractor(column):
    '''En la columna month_added en la que los datos vienen como "mes día" extrae
    los meses que luego convertimos en número'''
    column = column.str.extract(r'(\w+)')
    return column

def string_convert(column):
    '''Esta función convierte a string los datos de la columna'''
    column = column.apply(str)
    return column



