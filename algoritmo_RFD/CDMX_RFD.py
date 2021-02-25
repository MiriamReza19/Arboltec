# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:39:52 2020

@author: PCmar
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

cdmx = pd.read_csv('/home/miriam/Escritorio/app/algoritmo_RFD/RFD.csv')
#Eliminamos la primera columna ID
#cdmx = cdmx.drop('id',axis=1)
#Declaramos nuestros areglos a utilizar
#arx seran nuestras caracteristicas para entrenar nuestro modelo
arx = np.array(cdmx.drop(['Arboles'],1))
#ary seran nuestras etiquetas 
ary = np.array(cdmx['Arboles'])

X_train, X_test, y_train, y_test = train_test_split(arx, ary, test_size=0.3)
print('Son {} datos para entrenamiento y {} datos para prueba'.format(X_train.shape[0], X_test.shape[0]))

arbol = RandomForestClassifier(n_estimators=100, bootstrap = True, verbose=2,max_features = 'sqrt')
arbol.fit(X_train,y_train)

Y_pred = arbol.predict(X_test)
print('Precisión random forest: {}'.format(arbol.score(X_train, y_train)))

