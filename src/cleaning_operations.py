import numpy as np


def nullPer(df, columns):
    '''Esta función sirve para calcular el porcentaje 
    de datos nulos de las columnas'''
    for i in columns:
        null_rate = df[i].isna().sum() / len(df) * 100 
        if null_rate > 0 :
            print(f"{i}'s null rate : {null_rate}%")

def stripObject(df, columns):
    '''Función para quitar los espacios antes y después
    de los valores de las columnas'''
    for column in columns:
        if df[column].dtype == np.object:
            df[column] = df[column].str.strip()
    return df

