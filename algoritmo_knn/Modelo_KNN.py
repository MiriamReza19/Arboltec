# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:10:53 2020

@author: PCmar
"""
import pandas as pd
import numpy as np

import joblib


def prediction(pnt):
#Llamamos a nuetro modelo ya entrenado
    clf = joblib.load('C:/Users/peluc/OneDrive/Desktop/proyecto/algoritmo_knn/KNN_model.pkl')
#Llamamos a el set de datos
    cdmx = pd.read_csv('C:/Users/peluc/OneDrive/Desktop/proyecto/algoritmo_knn/Data_KNN.csv')
#Eliminamos la primera columna ID
    cdmx = cdmx.drop('id',axis=1)
#Declaramos como arreglos las columnas necesarias
    arx = np.array(cdmx.drop(['CLAVE'],1))
    ary = np.array(cdmx['CLAVE'])
#Es el procentaje de efectividad con el dataset completo
    clf.score(arx,ary)
#Es el arrglego que se probara
    Y_pred = clf.predict([pnt])
   # print("Array",Y_pred)
    return(Y_pred)
        
r=prediction([ 19.355975, -99.110870])
print("Array",r)