# Score más alto
# Una de las tribus está diseñando un detector de veneno. Ellos lograron
# identificar las 10 características mínimas y requeridas que hacen de 
# una sustancia una sustancia venenosa para su especie (veneno.csv). 
# Tu has recibido un dataset (sustancias_diversas.csv) de 500 sustancias 
# diversas con las 10 características, estas sustancias fueron encontradas en
# distintos lagos cada una. La idea es clausurar lagos infectados. La tropa 
# que cerrará los lagos infectados tiene sólo 50 miembros, tu debes entregar
# un dataset con las primeros 50 lagos que cerrará cada miembro de la tropa.

import pandas as pd

def prueba1():
  
  # Se leen los datos mediante la libreria pandas
  # En sustancias se almacenan las sustancias diversas
  # En veneno la características para considerar una sustancia venenosa
  sustancias = pd.read_csv("./sustancias_diversas.csv")
  venenos = pd.read_csv("./veneno.csv")

  # Se hace una limpieza de datos en sustancias quitando la columna id
  sustanciasNew = sustancias.drop(columns=["id"])

  limitCounter = []

  # La estrategia es por cada sustancia comparar cada caracteristica
  # contra la misma característica del veneno y si supera se agrega a
  # un contador. Es decir si una sustancia supero en 8 caracteristicas a 
  # la del veneno, tendrá un contador de 8.

  # Al final se ordenan en base a los que tengan el contador más alto.

  # Dentro de los análisis futuros se encuentra el dicernir dentro de los
  # que tengan el mismo contador cuales se consideran más graves dependiento
  # de que tan alejado se encuentran del patrón.

  for i in range(500):
    counter = 0
    for column in sustanciasNew:
      # Se compara cada característica con la del patrón
      if (sustanciasNew[column][i] > venenos[column][0]):
        counter = counter + 1
    limitCounter.append(counter)
  newColum = pd.Series(limitCounter)
  sustancias['Counter'] = newColum.values
  results = sustancias[['id', 'Counter']]
  results = results.sort_values(by=['Counter'], ascending=False)
  results = results.iloc[0:50]
  print(results)
  results.to_csv("urgente_orden_cierre.csv", index=False)

prueba1()

