from matplotlib import pyplot as plt
import pandas as pd 



def export_plots(df):
    """ Esta función permite exportar archivos CSV
    """
    name=input('Introduce el nombre del plot para guardar')
    format=input('Introduce el formato en el que quieres guardar el plot')
    return f"{name}.{format}, bbox_inches='tight')

def open_cvs():
    """ Esta función permite abrir el archivo CSV que le indiques, de la carpeta
        que le indiques
    """
    folder=input('Introduce el nombre de la carpeta en la que se encuentra tu archivo CSV: ')
    name=input('Introduce el nombre del archivo CSV que quieres abrir: ')
    return pd.read_csv(f'{folder}/{name}.csv',encoding='latin-1')

def getData(listed_in,release_year):
    """
    Extrae la información del dataset en función del año
    y el género indicados.
    """
    data_filter = netflix_title[(netflix_title["listed_in"] == listed_in) & (netflix_title["release_year"] == release_year)]
    return data_filter

