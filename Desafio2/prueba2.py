# Una tribu pacífica de la isla tiene un concurso legendario de jamones. 
# El jurado es muy longevo y este año ha perdido a más de la mitad de sus
#  miembros. La tribu te ha enviado una base de datos (score_de_jamonosidad.csv)
# de los últimos concursos. En esta base de datos se enlistan distintos
#  especímenes de jamones con la calificación que el jurado otorgó a
# cada uno. También has recibido una base de datos de jamones no calificados
# (jamones_por_calificar.csv) que deberás calificar, honrando el espíritu del jurado.

# Importar la libreria pandas para lectura de datos, sklearn para aplicar
# el método de entrenamiento y hacer la predicción de puntuación
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree

def prueba1():
  # Se cargan los archivos csv para el entrenamiento y el que se va a calificar
  calificados = pd.read_csv("./score_de_jamonosidad.csv")
  por_calificar = pd.read_csv("./jamones_por_calificar.csv")

  # se crean los sets den entrada que contiene las características v1, v2, v3
  # y el valor obtenido por cada uno de acuerdo a la puntuación
  x = calificados[['v1', 'v2', 'v3']]
  y = calificados[['score']]

  # se crea el set que va a ser calificado por medio de la predicción
  x_calificar = por_calificar[['v1', 'v2', 'v3']]

  # Se utiliza train_test_split para crear los sets de entrenamiento y prueba
  # utilizando un 30 porciento para prueba y el resto para entrenamiento
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

  # Para este ejercicio se utiliza un árbol de decisión con una profundidad de 5
  # utilizamos tree de la libreria sklearn y el DecisionTreeClassifier
  classifier = tree.DecisionTreeClassifier(max_depth=5)
  
  # Se pasan los sets de entrenamiento
  classifier.fit(x_train, y_train)
  # Se utilizan los sets de prueba para medir el entrenamiento
  classifier.score(x_test, y_test)

  #Se crea la predicción para el set que se va a calificar
  y_result = classifier.predict(x_calificar)
  print("y_result")
  print(y_result)

  print(classifier.score(x_calificar, y_result))
prueba1()

