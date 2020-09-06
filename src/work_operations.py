from matplotlib import pyplot as plt
import pandas as pd 



'''def export_plots(df):
    """ Esta función permite exportar archivos CSV
    """
    name=input('Please, enter the name of the figure you want to export')
    savefig('foo.png', bbox_inches='tight')

    df.to_csv(f"src/{name}.csv",index = False, header =  True)
    return f"{name} has been exported to cvs file"'''

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


'''def df_filter(df, string):
    new = df.filter(regex=string)
    return new'''


'''def plotBar(df.column1, df.column2)

    plt.title("Ventas en tienda")
    plt.xlabel("Meses")
    plt.ylabel("€")'''


'''def graficoDatos(item,year):
    """
    Gráfico tipo pie que muestra la cantidad de alimentos feed
    y food y sus porcentajes.
    """
    data_filter = datasp[datasp["Item"] == f"{item}"]
    toneladas = list(data_filter[f"Y{year}"])
    total = sum(toneladas)
    if len(toneladas) == 1:
        toneladas = [0] + list(data_filter[f"Y{year}"])
    labels = "Feed","Food"
    colors = ['lightseagreen','hotpink']
    explode = (0.1, 0) 
    plt.pie(toneladas, labels=labels,colors=colors,explode=explode,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(f"{item} {total}k t. en el año {year}")
    plt.savefig("graficodatos")
    print(f"{toneladas[0]}k tonnes Feed - {toneladas[1]}k tonnes Food")

def graficoBonus(item,year):
    """
    Gráfico de barras comparando la producción del producto en feed/food
    en los próximos 10 años al definido.
    """
    col_food = []
    col_feed = []
    year = int(year)
    if year < 2004:
        years = list(range(year,(year+10)))
    else:
        years = list(range(year,2014))
    bonus_filter = datasp[datasp['Item']== f"{item}"]
    if (len(bonus_filter)) == 1:
        indice = bonus_filter.index[0]
        if bonus_filter.Element[indice] == 'Food':
            for ye in years:
                ton_bonus = list(bonus_filter[f"Y{ye}"])
                for ton in ton_bonus:
                    col_food.append(ton)
                    col_feed.append(0)
        elif bonus_filter.Element[indice] == 'Feed':
            for ye in years:
                ton_bonus = list(bonus_filter[f"Y{ye}"])
                for ton in ton_bonus:
                    col_food.append()
                    col_feed.append(ton)
    else:
        for ye in years:
            ton_bonus = list(bonus_filter[f"Y{ye}"])
            col_feed.append(ton_bonus[0])
            col_food.append(ton_bonus[1])

    grafic = pd.DataFrame(col_feed, index=years, columns=["Feed"])
    grafic["Food"] = col_food
    grafic.plot.bar(color = ['lightseagreen','hotpink'])
    plt.title(f"Evolución de la producción desde {year}")
    plt.savefig("graficodatosbonus")

def requestINEh(year):
    global resh
    date = f"{year}0101:{year}1231"
    codigo = "CP300335"
    url= f'http://servicios.ine.es/wstempus/js/ES/DATOS_SERIE/{codigo}?date={date}'
    print(f"Requesting data from {url}")
    resh = requests.get(url)
    if resh.status_code != 200:
        print(resh.text)
        raise ValueError("Bad Response")
    return resh.json()'''