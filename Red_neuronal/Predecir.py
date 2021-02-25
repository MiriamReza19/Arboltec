# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 12:04:40 2020

r
"""
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

longitud, altura = 21, 28
modelo = 'C:/Users/peluc/OneDrive/Desktop/proyecto/Red_neuronal/modelo/modelo.h5'
pesos_modelo = 'C:/Users/peluc/OneDrive/Desktop/proyecto/Red_neuronal/modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("Acacia azul")
  elif answer == 1:
    print("Acacia Negra")
  elif answer == 2:
    print("Ahuehuete")
  elif answer == 3:
    print("Ahuejote")
  elif answer == 4:
    print(" Aile")
  elif answer == 5:
    print("Arbol Orquidea")
  elif answer == 6:
    print("Astronomica")
  elif answer == 7:
    print("Ayacahuite")
  elif answer == 8:
    print("Capulin")
  elif answer == 9:
    print(" Cazahuate")
  elif answer == 10:
    print("Cedro blanco")

  return answer

#predict('C:/Users/peluc/Downloads/Cazahuate_04.jpg')