from fastapi import FastAPI, Response
import pandas as pd
import numpy as np
import ast
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import LabelEncoder
import json

#http://127.0.0.1:8000

app = FastAPI(
    title = "Acceso a datos e informacion de la empresa respecto peliculas, series y productoras",
    description = "Proyecto de disponibilizacion de los datos de la empresa",
    )

# PROBANDO EL SERVIDOR EN ROOT "/"
@app.get('/')
async def root():
    return Response(content = '<h1 align="center">Inicio exitoso del servidor de FastAPI</h1>', media_type = 'text/html')

@app.get('/cantidad_filmaciones_mes/{mes}')
def peliculas_mes(mes: str):
    archivo='./Datos/sistemaconsulta_func1234.csv'
    columnas=['release_date']
    data = pd.read_csv(archivo, low_memory=False, usecols=columnas)
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    meses_dict = {
        'january': 'enero',
        'february': 'febrero',
        'march': 'marzo',
        'april': 'abril',
        'may': 'mayo',
        'june': 'junio',
        'july': 'julio',
        'august': 'agosto',
        'september': 'septiembre',
        'october': 'octubre',
        'november': 'noviembre',
        'december': 'diciembre'
    }
    mes_espanol = meses_dict.get(mes.lower(), mes)
    cantidad_peliculas = len(data[data['release_date'].dt.month_name().str.lower() == mes.lower()])
    return {'mes':mes_espanol, 'cantidad':cantidad_peliculas}

@app.get('/cantidad_filmaciones_dia{dia}')
def peliculas_dia(dia:str):
    archivo='./Datos/sistemaconsulta_func1234.csv'
    columnas=['release_date']
    data = pd.read_csv(archivo, low_memory=False, usecols=columnas)
    data['release_date'] = pd.to_datetime(data['release_date'], errors='coerce')
    dias_dict = {
        'monday': 'lunes',
        'tuesday': 'martes',
        'wednesday': 'miércoles',
        'thursday': 'jueves',
        'friday': 'viernes',
        'saturday': 'sábado',
        'sunday': 'domingo'
    }
    dia_espanol = dias_dict.get(dia.lower(), dia)
    cantidad_dias = len(data[data['release_date'].dt.day_name().str.lower() == dia.lower()])
    return {'dia':dia_espanol, 'cantidad':cantidad_dias}    

@app.get('/score_titulo/{titulo}')
def score_titulo(pelicula: str):
    archivo = './Datos/sistemaconsulta_func1234.csv'
    columnas=['title', 'release_year', 'popularity']
    data = pd.read_csv(archivo, low_memory=False, usecols=columnas)
    pelicula_data = data[data['title'].str.lower() == pelicula.lower()]
    
    if pelicula_data.empty:
        return f"No se encontró información de la película {pelicula}"
    
    titulo = pelicula_data['title'].iloc[0]
    anio = pelicula_data['release_year'].iloc[0]
    score = pelicula_data['popularity'].iloc[0]

    return {'titulo':titulo, 'anio':anio, 'popularidad':score}

@app.get('/votos_titulo/{titulo}')
def votos_titulo(pelicula: str):
    archivo = './Datos/sistemaconsulta_func1234.csv'
    columnas=['title', 'release_year', 'vote_count', 'vote_average']
    data = pd.read_csv(archivo, low_memory=False, usecols=columnas)
    pelicula_data = data[data['title'].str.lower() == pelicula.lower()]
    pelicula_count = data[data['title'].str.lower() == pelicula.lower()]['vote_count'].sum()
    if pelicula_data.empty:
        return f"No se encontró información de la película {pelicula}"
    if pelicula_count < 2000:
        return f"No se encontró información de la película {pelicula}"
    
    titulo = pelicula_data['title'].iloc[0]
    anio = pelicula_data['release_year'].iloc[0]
    count = pelicula_data['vote_count'].iloc[0]
    average = pelicula_data['vote_average'].iloc[0]

    return {'titulo':titulo, 'anio':anio, 'voto_total':count, 'voto_promedio':average}

@app.get('/get_actor/{nombre_actor}')
def get_actor(nombre_actor: str):
    archivo = './Datos/sistemaconsulta_cast.csv'
    columnas = ['cast', 'return']
    data = pd.read_csv(archivo, low_memory=False, usecols=columnas)
    actor_films = data[data['cast'].str.contains(nombre_actor, case=False)]['return']
    cantidad_peliculas = actor_films.count()
    
    if cantidad_peliculas == 0:
        return f"No se encontró información del actor {nombre_actor}"
    
    retorno_total = actor_films.sum()
    promedio_retorno = retorno_total / cantidad_peliculas

    return {'actor': nombre_actor, 'cantidad_filmaciones': cantidad_peliculas, 'retorno_total': retorno_total, 'retorno_promedio': promedio_retorno}

@app.get('/get_director/{nombre_director}')
def get_director(nombre_director: str):
    archivo = './Datos/sistemaconsulta_directors.csv'
    columnas = ['director', 'title', 'release_date', 'budget', 'revenue', 'return']
    data = pd.read_csv(archivo, low_memory=False, usecols=columnas)

    director_films = data[data['director'].str.lower() == nombre_director.lower()]
    if director_films.empty:
        return json.dumps({
            'director': nombre_director,
            'retorno_total_director': 0,
            'peliculas': [],
            'anio': [],
            'retorno_pelicula': [],
            'budget_pelicula': [],
            'revenue_pelicula': []
        })

    retorno_total_director = director_films['return'].sum()
    peliculas = director_films['title'].tolist()
    anio = director_films['release_date'].tolist()
    retorno_pelicula = director_films['return'].tolist()
    budget_pelicula = director_films['budget'].tolist()
    revenue_pelicula = director_films['revenue'].tolist()

    result = {
        'director': nombre_director,
        'retorno_total_director': retorno_total_director,
        'peliculas': peliculas,
        'anio': anio,
        'retorno_pelicula': retorno_pelicula,
        'budget_pelicula': budget_pelicula,
        'revenue_pelicula': revenue_pelicula
    }

    return json.dumps(result)

# ML
@app.get('/recomendacion/{titulo}')
def recomendacion(titulo: str):
    archivo = './Datos/sistemarecomendacion.csv'
    columnas = ['title', 'genres', 'popularity', 'vote_average']  # Reemplaza 'feature1', 'feature2', 'feature3' con las características relevantes de las películas

    # Leer el archivo CSV y seleccionar las columnas de interés
    data = pd.read_csv(archivo, low_memory=False, usecols=columnas)

    # Codificar las etiquetas de la columna 'genres'
    label_encoder = LabelEncoder()
    data['genres_encoded'] = label_encoder.fit_transform(data['genres'])

    # Crear un modelo de vecinos más cercanos
    model = NearestNeighbors(n_neighbors=4, algorithm='brute')  # Ajusta el número de vecinos y el algoritmo según tus necesidades

    # Ajustar el modelo a los datos
    model.fit(data[['genres_encoded', 'popularity', 'vote_average']])  # Reemplaza 'feature1', 'feature2', 'feature3' con las características relevantes de las películas

    # Buscar las películas similares al título dado
    indice = data[data['title'] == titulo].index[0]
    _, indices_similares = model.kneighbors(data.iloc[indice][['genres_encoded', 'popularity', 'vote_average']].values.reshape(1, -1))

    # Obtener los títulos de las películas similares
    peliculas_similares = data.loc[indices_similares[0], 'title'].tolist()

    return {'lista_recomendada': peliculas_similares}