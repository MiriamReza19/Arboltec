 # -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:49:08 2020

@author: PCmar"""

import pandas as pd
import numpy as np
import joblib

def RFDprediction(pnt):
#Llamamos a nuetro modelo ya entrenado
    clf = joblib.load('C:/Users/peluc/OneDrive/Desktop/proyecto/algoritmo_RFD/RFD_model.pkl')
#Llamamos a el set de datos
    arboles = pd.read_csv('C:/Users/peluc/OneDrive/Desktop/proyecto/algoritmo_RFD/RFD.csv')
#Eliminamos la primera columna ID
#    cdmx = cdmx.drop('id',axis=1)
#Declaramos como arreglos las columnas necesarias
    arx = np.array(arboles.drop(['Arboles'],1))
    ary = np.array(arboles['Arboles'])
#Es el procentaje de efectividad con el dataset completo
    clf.score(arx,ary)
#Es el arrglego que se probara
    Y_pred = clf.predict([pnt])
 #   print(Y_pred)
    return(Y_pred)

P = RFDprediction([9, 1000, 1200])
print(P)