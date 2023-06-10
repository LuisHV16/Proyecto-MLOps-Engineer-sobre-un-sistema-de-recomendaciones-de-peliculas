![header](https://connectjaya.com/wp-content/uploads/2021/07/Slide1.jpg)

## Índice:
<!-- TABLA DE CONTENIDOS -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li><a href="#Índice">Indice</a></li>
    <li><a href="#Introducción">Introducción</a></li>
    <li><a href="#Objetivos">Objectivo</a></li>
    <li><a href="#Tech Stack">Tecnologías utilizadas</a></li>
    <li><a href="#ETL">ETL</a></li>
    <li><a href="#EDA">EDA</a></li>
    <li><a href="#API Funtiones">API Funciones</a></li>
    <li><a href="#Sistema de recomendaciones">Sistema de recomendaciones</a></li>
    <li><a href="#Deployment">Deployment</a></li>
    <li><a href="#Video">Video resumen del proyecto</a></li>
    <li><a href="#Desarrollador">Desarrollador del proyecto</a></li>
  </ol>
</details>

## Introducción 
<p align="justify">
Este proyecto forma parte de la etapa de Labs de la academia de formación Henry en ciencia de datos, siendo el primer proyecto individual propuesto para la implementación de un análisis de datos. </br>

Para este primer proyecto se entregó a los estudiantes una base de datos en formato CSV del cual se debía llevar a cabo los procesos de transformacion y limpieza de datos (ETL), asi como la exploracion de los datos (EDA), implementación de un sistema de recomendaciones de peliculas e implementación para su consumo virtual por medio de una API en Render.
</p>

## Objetivos
El objetivo principal de este proyecto es desarrollar e implementar un sistema de recomendación de películas basado en el contenido aprovechando los datos de un conjunto completo de datos de películas, para llevar esto a cabo debemos además realizar algunos objetivos basicos con la data proporcionada para este proyecto, dichos objetivos son:
- Transformación y limpieza de datos (ETL): aplicar técnicas de extracción, transformación y carga para preprocesar y limpiar el conjunto de datos de películas.
- Análisis exploratorio de datos (EDA): realizar un análisis exploratorio de los datos con el fin de identificar las características clave que influyen significativamente en las preferencias de películas y encontrar relaciones entre los datos que se pueden aprovechar para obtener recomendaciones precisas.
- Desarrollo de API: Diseñar e implementar un conjunto de funciones y e implementarlo con el servicio FastAPI.
- Generacion de un sistema de recomendaciones: Desarrollar un modelo de aprendizaje automático que utilice técnicas de filtrado basadas en contenido y puntajes de similitud para recomendar películas con atributos similares a los proporcionados por el usuario.
- API deployment: Implementar la API del sistema de recomendaciones en un entorno de producción, asegurando que esté disponible y accesible para los usuarios, para esta etapa del proceso utilizaremos los servicios de Render.

## Tech Stack
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

- seaborn 
- tabulate
- Json
- Wordcloud

## ETL
El proceso ETL se realizó en el conjunto de datos dado para prepararlo para el análisis y la consulta, siguiendo los pasos a continuación:
1. Para simplificar el conjunto de datos y centrarse en la información relevante, se eliminaron las columnas innecesarias, como "video," "imdb_id," "adult," "original_title," "vote_count," "poster_path," and "homepage".
2. Los valores nulos en los campos "revenue" y "budget" se reemplazaron por 0, lo que garantiza la coherencia en los cálculos. Los valores nulos en el campo "release_date" se eliminaron para garantizar la integridad de los datos.
3. Para estandarizar el formato, las fechas se transformaron al formato AAAA-mm-dd. Además, se creó una nueva columna llamada "release_year" para extraer el año a partir de la fecha de lanzamiento, proporcionando un campo separado para el análisis temporal.
4. Se calculó una métrica crucial, el rendimiento de la inversión, dividiendo los ingresos por el presupuesto de cada entrada, lo que resultó en una nueva columna llamada "return". Cuando los datos no estaban disponibles para calcular el retorno, se le asignó un valor de 0, manteniendo la consistencia en el conjunto de datos.
5. El conjunto de datos contenía campos anidados, como "belongs_to_collection" y "production_companies", "cast" y "crew" que debían desanidarse para facilitar la manipulación de los datos.

Todo esto fue desarrollado localmente en VSCODE utilizando Jupyter Notebook, python, numpy y pandas.

## EDA
Para el desarrollo de nuestro Analisis exploratorio de datos comenzamos por analizar las columnas con datos numéricos para esto utilizamos diagramas de visualizacion son seaborn para identificar visualmente las relaciones mas evidentes entre las columnas, luego nos servimos de implementar un dataframe de correlaciones donde pudimos ver numericamente las correlaciones mas resaltantes de nuestros datos, aplicamos un diagrama de calor para visualizar las columnas donde se tiene una relacion mas fuerte entre los datos y posteriormente nos servimos de diagramas de dispersion tomados dos a dos con las columnas que guardaban mayor relacion entre ellas con la finalidad de obtener conclusiones mas asertivas sobre dichos datos, posteriormente creamos dataframes con las columnas que servirian para nuestro proceso de implementacion de modelos de consulta y exportamos esta data en distintos archivos para que el proceso de acceso a dichos datos sea mas eficiente y consuma menos recursos computacionales, finalmente decidimos implementar algunas preguntas relevantes sobre nuestra data obteniendo interesantes resultados y conclusiones que se pueden encontrar en nuestro archico correspondiente a esta parte llamado "Analisis Exploratorio"

Todo esto fue desarrollado localmente en VSCODE utilizando Jupyter Notebook, python, numpy, pandas, matplotlib, seaborn y wordcolud.

## API Funciones
Para esta parte del proyecto implementamos un entorno virtual al cual agregamos las librerias necesarias para llevar a cabo nuestro proyecto y desarrollamos funciones que serian consumidas de forma virtual por el servidor del servicio de FastAPI al cual adjuntaremos el enlace para poder visualizar dichas funciones dando clic al archivo [main.py](https://github.com/LuisHV16/Proyecto-MLOps-Engineer-sobre-un-sistema-de-recomendaciones-de-peliculas/blob/main/main.py) este archivo contiene los modelos de consulta al cual son consumidos para poderlos visualizar en el servidos ASGI de FastAPI, este era un punto importante solicitados por la direccion del proyecto, ademas es posible visualizar y ejecutar de forma local las funciones creadas para el modelo de consulta dando clic al archivo [funciones.py](https://github.com/LuisHV16/Proyecto-MLOps-Engineer-sobre-un-sistema-de-recomendaciones-de-peliculas/blob/main/Modelos%20de%20Consulta.ipynb). 

Todo esto fue desarrollado localmente en VSCODE usando Jupyter Notebook, python, numpy, pandas, FastAPI, uvicorn, tableau, json.

## Sistema de recomendaciones de películas
Para nuestro modelo de recomendaciones de peliculas primero creamos un archivo tomando en cuenta unicamente las columnas que serian utilizadas por nuestro modelo, propusimos un modelos de recomendaciones basicas tomando en cuenta las columnas 'title', 'genres', 'popularity', 'vote_average' ya que considere que es el criterio predominante en un usuario standar al momento de seleccionar una pelicula y creamos un modelo de machine learning utilizando NearestNeighbors de 4 vecinos que compartan caracteristicas similares al del titulo solicitado por el usuario. El desarrollo de nuestro modelo pueden encontrarlo en el siguiente archivo: [Machine Learning Development](https://github.com/LuisHV16/Proyecto-MLOps-Engineer-sobre-un-sistema-de-recomendaciones-de-peliculas/blob/main/Modelo%20de%20ML.ipynb) on this repository.

Este modelo fue desarrollado en VSCODE utilizando Jupyter Notebook, python, numpy, pandas y scikit-learn.

## Deployment
Luego de implementar nuestros modelos de consulta y de recomendaciones de peliculas utilizando los servicios de FastAPI mediante la creacion de nuestro archivo main.py procedemos a hacer el despliegue del proyecto utilizando los servicios de Render para que pueda ser utilizado de forma remota y virtual, para esto creamos un archivo de nombre [requierements.txt](https://github.com/LuisHV16/Proyecto-MLOps-Engineer-sobre-un-sistema-de-recomendaciones-de-peliculas/blob/main/requirements.txt) ya que este archivo contiene las librerias necesarias para el funcionamiento de todo nuestro entorno virtual y nos otorga la ventaja de que los colaboradores que decidan unirse a este proyecto y hacerlo mas robusto pueden crear un entorno virtual con las librerias indicadas en dicho archivo y poder a partir de los archivos compartidos en nuestro respositorio de github, dicho esto es posible acceder a nuestra API creada y consumida desde Render dando clic al siguiente enlace [running API](https://proyecto-mlops-engineer-sobre-un-sistema.onrender.com/docs).  

## Desarrollador

Aqui comparto el enlace a mi perfil de LinkedIn, si acaso algun equipo de proyecto u empresa se sintiera interesado en mi talento y conocer un poco mas acerca de mi: </br>

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luis-arturo-huerto-valentin-1334811a5/)

</div>

## Video
En el siguiente enlace hago una rapida presentacion y explicacion sobre lo realizado en el proyecto, para que los interesados puedan acceder y conocer un poco más en mis palabras sobre los que se desarrollo en todo el proceso de analisis de este proyecto.

<div align="center">
  
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=B-hJy58UnNY)
  
</div>