![header](https://connectjaya.com/wp-content/uploads/2021/07/Slide1.jpg)

## Índice:
<!-- TABLA DE CONTENIDOS -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li><a href="#Index">Indice</a></li>
    <li><a href="#Introduction">Introducción</a></li>
    <li><a href="#Objective">Objectivo</a></li>
    <li><a href="#Tech Stack">Tecnologías utilizadas</a></li>
    <li><a href="#ETL">ETL</a></li>
    <li><a href="#EDA">EDA</a></li>
    <li><a href="#API Functions">API Funciones</a></li>
    <li><a href="#Recommendation System">Sistema de recomendaciones</a></li>
    <li><a href="#Deployment">Deployment</a></li>
    <li><a href="#Video">Video resumen del proyecto</a></li>
    <li><a href="#Developer">Desarrollador del proyecto</a></li>
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

## API Functions
Para esta parte del proyecto implementamos un entorno virtual al cual agregamos las librerias necesarias para llevar a cabo nuestro proyecto y desarrollamos funciones que serian consumidas de forma virtual por el servidor del servicio de FastAPI al cual adjuntaremos el enlace para poder visualizar dichas funciones dando clic al archivo [main.py](https://github.com/LuisHV16?tab=repositories) este archivo contiene los modelos de consulta al cual son consumidos para poderlos visualizar en el servidos ASGI de FastAPI, este era un punto importante solicitados por la direccion del proyecto, ademas es posible visualizar y ejecutar de forma local las funciones creadas para el modelo de consulta dando clic al archivo [funciones.py](https://github.com/LuisHV16?tab=repositories). 

Todo esto fue desarrollado localmente en VSCODE usando Jupyter Notebook, python, numpy, pandas, FastAPI, uvicorn, tableau, json.

## Recommendation System
The recommendation system was developed in a Jupyter Notebook file. The NLP tool RAKE was used to generate keywords from the overview column. These keywords were combined with the genres_name and title columns into a single string for each film. CountVectorizer was then used to calculate the cosine similarity matrix. Based on the similarity scores provided by the matrix, the algorithm recommends the top 5 most similar movies to the one provided by the user as input. This model was also made available as an endpoint on the API. The completed algorithm the API uses is located in a python file called recomendacion.py in the API repository. The development of the algorithm is on this repository: [Machine Learning Development](https://github.com/ksfajardo/PI01_ML_OPS/blob/main/MLmodel.ipynb) on this repository.

All of this was developed locally in VSCODE using Jupyter Notebook, python, numpy, pandas, rake-nltk and scikit-learn.

## Deployment
After having the main.py and the rest of the files with the model and functions complete, the API was deployed using Google Cloud Run, as it offers the flexibility to allocate a desired amount of RAM memory and CPUs to the application. Since Cloud Run is a container hosting service, it was necessary to set up the API environment in a docker file. To do this, a [requierements.txt](https://github.com/ksfajardo/PI01_ML_OPS_API/blob/main/requirements.txt) file was constructed inside of which all the dependencies and libraries necessary to run the endpoints were included. Then, the docker image was created locally and subsequently uploaded to Docker Hub. 
Next, on Google Cloud, a Cloud Run service was created with the link given by Docker Hub of the docker image. 16GiB of RAM memory and 4 CPUs were assigned to run the API. Whit this, Cloud Run itself deploys the application and generates a link to acces the [running API](https://moviesapp-oxeinkhcia-uc.a.run.app).  

PD: It is worth mentioning that even with all of this resources the service was unable to run the recommendation algorithm using the full dataset (the similarity matrix of the full dataset alone weighs almost 15GB). Even though I could have allocated even more resources to the API so that it runs in its full dataset glory, I did not because that would have meant having to search for a server (in all of the possible regions that Google Cloud has, which are A LOT) that could host it, because every region has a different limit of resources allowed per user. So, instead I decided to use a sample of the dataset (half its size to be precise) and deploy the API with it. You can find this part in the last section of the Jupyter Notebook where the recommedation system was developed ([here](https://github.com/ksfajardo/PI01_ML_OPS/blob/main/MLmodel.ipynb)).

## Developer
<div align="center">
Only me this time :) 
 
| [<img src="https://avatars.githubusercontent.com/u/104804355?s=400&u=7c7592e2239f0ef414c4a3c5a61920ab19c9d980&v=4" width=115><br><sub>Karla Fajardo</sub>](https://github.com/ksfajardo) |
| :---: | 

Here is my Linkedin if you would like to get in contact with me: </br>

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/karla-fajardo-3b3020175/)

</div>

## Video
If you would like to see the video of me giving an overview of this project, click on the YouTube logo below:

<div align="center">
  
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=B-hJy58UnNY)
  
</div>

(In the video I talk in spanish)

## Acknowledgment

Here are a few people I would like to thank for their unwavering support throughout the development of this project: </br>

First, to my beloved Full-Stack Developer boyfriend, William, who talked me out of using Render for my API and told me to go for something more challenging: Thank you, you were right. Docker and Google Cloud are indeed the GOAT. </br>

Second, to my favorite artist, Taylor Swift: thank you for meeting me at midnight during every single day I spent developing this porject and keeping me company with your music while everybody else in my house slept. </br>

And last but not least, to the amazing friends I have made at Henry: Here is to helping and lifting each other up whenever we need it! I had the most fun helping you get to the finish line with me.

<div align="center">

![wink](https://github.com/ksfajardo/PI01_ML_OPS/blob/main/taylor.gif)

</div>