from matplotlib import pyplot as plt
import pandas as pd 
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def open_cvs():
    """ Esta función permite abrir el archivo CSV que le indiques, de la carpeta
        que le indiques
    """
    folder=input('Introduce el nombre de la carpeta en la que se encuentra tu archivo CSV: ')
    name=input('Introduce el nombre del archivo CSV que quieres abrir: ')
    return pd.read_csv(f'{folder}/{name}.csv',encoding='latin-1')

def countPlt(dataframe):
    """ Esta función permite crear un plot de barras a partir de la columna que
        que le indiques. El parámetro que necesita es el nombre del dataframe.
    """
    x = input('Introduce la columna que quieras comparar: ')
    print(type(x))
    sns.set()
    sns.countplot(x= f"{x}", data= dataframe)

def piePlt(df):
    """ Esta función permite crear un pie plot con los ocho valores más frecuentes
        de la columna que le indiques. El parámetro que necesita es el nombre del dataframe.
    """
    columnName=input('Introduce el nombre de la columna con la que quieras trabajar: ')
    top_column = df[columnName].value_counts()[0:8]
    top_column.index
    fig = px.pie(df,values = top_column,names = top_column.index,labels= top_column.index)
    fig.update_traces(textposition ='inside',textinfo='percent+label')
    fig.show()

def jointPlt(df):
    """ Esta función permite crear un pie plot a partir de la columna que
        que le indiques.El parámetro que necesita es el nombre del dataframe.
    """
    column1=input('Introduce el nombre de la  columna que quieras en el eje x: ')
    column2=input('Introduce el nombre de la  columna que quieras en el eje y: ')
    sns.jointplot(f'{column1}',f'{column2}', data = df)


def wordCloud(df):
    """ Esta función permite crear una wordcloud a partir de la columna que
        que le indiques.El parámetro que necesita es el nombre del dataframe.
    """
    columnName= input('Introduce el nombre de la columna de la que quieres obtener las palabras: ')
    plt.rcParams['figure.figsize'] = (10, 10)
    wordcloud = WordCloud(stopwords=STOPWORDS,background_color = 'white', width = 1000,  height = 1000, max_words = 121).generate(' '.join(df[columnName]))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.title(columnName,fontsize = 20)
    plt.show()

def count2Plt(df):
    """ Esta función permite crear un count plot de los 25 valores más frecuentes de la columna
        que le indiques que le indiques.El parámetro que necesita es el nombre del dataframe.
    """
    columnName= input('Introduce el nombre de la columna con la que quieras trabajar: ')
    top_column = df[columnName].value_counts()[0:25]
    top_column.head()
    sns.set()
    plt.figure(figsize=(20,13))
    sns.countplot(x=columnName,data = df,order =df[columnName].value_counts().index[0:25])
    plt.xticks(rotation = 90)
    plt.title(columnName,fontsize = 20)

    plt.show()



