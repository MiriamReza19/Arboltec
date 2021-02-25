# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:39:52 2020

@author: PCmar
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

arboles = pd.read_csv('RFD.csv')
#Eliminamos la primera columna ID
#arboles = arboles.drop('id',axis=1)
#Declaramos nuestros areglos a utilizar
#arx seran nuestras caracteristicas para entrenar nuestro modelo
arx = np.array(arboles.drop(['Arboles'],1))
#ary seran nuestras etiquetas 
ary = np.array(arboles['Arboles'])

print (arx)
print (ary)

X_train, X_test, y_train, y_test = train_test_split(arx, ary, test_size=0.2)
print('Son {} datos para entrenamiento y {} datos para prueba'.format(X_train.shape[0], X_test.shape[0]))

arbol = RandomForestClassifier(n_estimators=3, bootstrap = True, verbose=2,max_features = 'sqrt')
arbol.fit(X_train,y_train)

  
Y_pred = arbol.predict(X_test)
print('Precisión random forest: {}'.format(arbol.score(X_train, y_train)))

def save_model(clf):
    joblib.dump(clf, 'RFD_model.pkl')

save_model(arbol)
