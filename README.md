<p align="center">
  <img width="445" height="203" alt="image" src="https://github.com/user-attachments/assets/51feace9-2375-435e-a95a-695bb33f0a52" />
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Proyecto_Completado-%E2%9C%94-2ECC71?style=flat-square&logo=checkmarx&logoColor=white" alt="Proyecto Completado"/>
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Pandas-Análisis_de_Datos-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas"/>
  <img src="https://img.shields.io/badge/scikit--learn-Modelo_ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="scikit-learn"/>
  <img src="https://img.shields.io/badge/NLTK-Natural_Language_Toolkit-5C2D91?style=flat-square&logo=nltk&logoColor=white" alt="NLTK"/>
  <img src="https://img.shields.io/badge/WordCloud-Visualización_de_Nubes-3AA0E6?style=flat-square&logo=wordcloud&logoColor=white" alt="WordCloud"/>
</p>

Un análisis de datos de más de un millón de reseñas de cine para construir un modelo de predicción de sentimiento y descubrir los patrones ocultos en el lenguaje de la crítica.

### [Notebook](https://github.com/Ricardouchub/rotten-tomatoes-critics-nlp/blob/main/Notebook.ipynb)

---

## **Índice**
1. [Descripción del Proyecto](#1-descripción-del-proyecto)
2. [Dataset](#2-dataset)
3. [Análisis Exploratorio](#3-análisis-exploratorio)
4. [Modelado y Evaluación](#4-modelado-y-evaluación)
5. [Hallazgos y Conclusiones Principales](#5-hallazgos-y-conclusiones-principales)
6. [Herramientas](#6-herramientas)
7. [Autor](#8-autor)

---

## **1. Descripción del Proyecto**
El objetivo de este proyecto es explorar el vasto mundo de la crítica cinematográfica utilizando técnicas de **Procesamiento de Lenguaje Natural (NLP)** y **Machine Learning**. El análisis se centra en dos frentes:

* **Predictivo:** Construir y evaluar un modelo capaz de clasificar con alta precisión el sentimiento de una reseña (como 'Fresh' o 'Rotten') basándose únicamente en su contenido textual.
* **Investigativo:** Utilizar el modelo y los datos para responder preguntas más complejas: ¿Cómo ha evolucionado el lenguaje de la crítica a lo largo del tiempo? ¿Qué géneros y películas son los más polarizantes? ¿Qué palabras son el verdadero sello de un éxito o un fracaso?

---

## **2. Dataset**
El proyecto utiliza el dataset **[Rotten Tomatoes Movies and Critic Reviews](https://www.kaggle.com/datasets/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset)** disponible públicamente en Kaggle. Contiene dos archivos principales:

* `rotten_tomatoes_movies.csv`: Información sobre las películas, incluyendo título, género, director, etc.
* `rotten_tomatoes_critic_reviews.csv`: Más de 1.1 millones de reseñas individuales, con datos del crítico, la publicación, la fecha y el contenido de la crítica.

---

## **3. Análisis Exploratorio**
Antes del modelado, se realizó un proceso de limpieza y preparación:

* **Análisis Exploratorio (EDA):** Se investigó la distribución de las reseñas, la cantidad de datos nulos y las características generales del texto.
* **Limpieza de Texto:** Se implementó un pipeline de NLP para estandarizar las reseñas, incluyendo:
    * Conversión a minúsculas.
    * Eliminación de puntuación y caracteres no alfabéticos.
    * Eliminación de *stopwords* (palabras comunes sin valor predictivo).
    * Lematización para reducir las palabras a su forma raíz.
* **Ingeniería de Características:** Se creó la variable objetivo `sentimiento` (1 para 'Fresh', 0 para 'Rotten') a partir de la columna `review_type`.

---

## **4. Modelado y Evaluación**
Se entrenaron y compararon dos modelos de clasificación para encontrar el de mejor rendimiento:

1.  **Regresión Logística:** Un modelo lineal robusto y altamente interpretable.
2.  **LightGBM:** Un modelo avanzado basado en árboles de decisión (Gradient Boosting).

#### **Resultados de la Evaluación**
Tras la evaluación, se llegó a una de las primeras conclusiones interesantes del proyecto: el modelo de **Regresión Logística superó al más complejo LightGBM**, alcanzando una **precisión global del 80.67%**. Este modelo fue seleccionado para todos los análisis posteriores debido a su superior rendimiento y facilidad de interpretación.

<p align="center">
  <img width="522" height="422" alt="image" src="https://github.com/user-attachments/assets/e4d68afc-5ac6-4b19-939e-ba317f70def2" />
</p>

---

## **5. Hallazgos y Conclusiones Principales**
El análisis profundo de los datos y del modelo entrenado reveló varios hallazgos clave:

* **El Lenguaje del Fracaso es Atemporal:** El vocabulario para describir una mala película (`fails`, `dull`, `boring`) se ha mantenido sorprendentemente estable durante los últimos 20 años.
* **El Elogio Evoluciona con la Cultura:** El lenguaje positivo es más dinámico. El análisis descubrió el **"Efecto Selma"**, donde la aclamada película de 2014 se convirtió en un estándar de calidad, siendo su nombre un fuerte predictor de una crítica positiva en esa época.
* **El Terror es el Rey de la Polémica:** El género **Horror** demostró ser el más polarizante, con una división de críticas casi perfecta de 50/50 entre 'Fresh' y 'Rotten'.
* **Perfil de Películas Divisivas:** Se identificó que las películas que más dividen a los críticos suelen ser de géneros de nicho (terror), comedias de alto concepto o dramas de autor controvertidos.

---

## **6. Herramientas**
* **Lenguaje:** Python 3.9
* **Librerías Principales:**
    * `Pandas` y `NumPy` para la manipulación de datos.
    * `NLTK` para el preprocesamiento de texto y etiquetado gramatical.
    * `Scikit-learn` para el modelado, vectorización (TF-IDF) y evaluación.
    * `Matplotlib` y `Seaborn` para la visualización de datos.
    * `WordCloud` para la creación de nubes de palabras.
* **Gestión de Archivos:** `Git` y `Git LFS`.

---

## **7. Autor**
**Ricardo Urdaneta**

[**LinkedIn**](https://www.linkedin.com/in/ricardourdanetacastro/)

---

## **Visualizaciones destacadas**
<p align="center">
<img width="573" height="586" alt="image" src="https://github.com/user-attachments/assets/458528f3-113c-488f-b89f-3898f894584b" />
  <img width="683" height="415" alt="image" src="https://github.com/user-attachments/assets/513c8cc2-d1aa-4d91-a852-a0cfd7a41c38" />

</p>
