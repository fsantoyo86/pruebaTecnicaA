# Las sirenas endémicas que rodean la isla donde se encuentra tu celda tienen
# un seductor canto con el que atraen a sus machos y aseguran la persistencia
# de sus especie. Ha emigrado, solicitando refugio, una especie de sirenas de
# otros lares. Esta especie emite un sonido que interfiere con el canto de las
# sirenas endémicas. El guardián del océano va a delimitar una región para cada
# especie y pide tu ayuda para distribuirlas. Tú recibiste una
# base de datos (sirenas_endemicas_y_sirenas_migrantes_historico.csv) que 
# el museo de historia natural te ha facilitado con características de 
# individuos de cada especie. Recibiste también una base de datos con los 
# individuos que el guardián va a clasificar (sirenas_endemicas_y_sirenas_migrantes.csv).
# Indica en esta última, a qué especie de sirena pertenece cada individuo.

#Se importa la libreria pandas para leer los csv, así como la libreía sklearn
# para utilizar los métodos de predicción o clasificación
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree

def prueba1():

  # Se cargan los archivos con el historico de especies y el archivo a clasificar
  historico = pd.read_csv("./sirenas_endemicas_y_sirenas_migrantes_historico.csv")
  clasificar = pd.read_csv("./sirenas_endemicas_y_sirenas_migrantes.csv")

  # se crean los datos de entrada con las características v1, v2, v3
  # y el set con el tipo de especie asociado dependiento de las caracterísitcas
  x = historico[['v1', 'v2', 'v3']]
  y = historico[['especie']]

  # se crea el set a clasificar dadas las características v1, v2, v3
  x_classificar = clasificar[['v1', 'v2', 'v3']]

  # Se utiliza el train_test_split de sklearn para crear los sets de
  # entrenamiento y prueba
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

  # Se crea el árbol de decisión que nos permitira clasificar las sirenas
  classifier = tree.DecisionTreeClassifier(max_depth=5)
  
  # Se le pasa al álbol de decisión los sets de entrenamiento
  classifier.fit(x_train, y_train)
  
  #Se realiza la predicción para el set a clasificar
  y_result = classifier.predict(x_classificar)
  print("y_result")
  print(y_result)

  print(classifier.score(x_classificar, y_result))
prueba1()

