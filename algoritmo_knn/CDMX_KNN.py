# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:59:53 2020

@author: PCmar
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.externals import joblib

import joblib


cdmx = pd.read_csv('Data_KNN.csv')
#Eliminamos la primera columna ID
cdmx = cdmx.drop('id',axis=1)
#Declaramos nuestros areglos a utilizar
#arx seran nuestras caracteristicas para entrenar nuestro modelo
arx = np.array(cdmx.drop(['CLAVE'],1))
#ary seran nuestras etiquetas 
ary = np.array(cdmx['CLAVE'])
#print(arx)
#print(ary)

#Designamos el 80% para aprendizaje (X_train y y_train) y el 20% para hacer la prueba (X_test y y_test)
X_train, X_test, y_train, y_test = train_test_split(arx, ary, test_size=0.2)
print('Son {} datos para entrenamiento y {} datos para prueba'.format(X_train.shape[0], X_test.shape[0]))

#Modelo de Vecinos más Cercanos
knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
Y_pred = knn.predict(X_test)
print('Precisión Vecinos más Cercanos: {}'.format(knn.score(X_train, y_train)))

#funcion para ver la grafica con nuestros puntos dados
def ghrafic_point(mx):
    
    fig = mx[mx.CLAVE == 2].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='blue', label='AZCAPOTZALCO')
    mx[mx.CLAVE == 3].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='green', label='COYOACAN', ax=fig)
    mx[mx.CLAVE == 4].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='red', label='CUAJIMALPA DE MORELOS', ax=fig)
    mx[mx.CLAVE == 5].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='fuchsia', label='GUSTAVO A. MADERO', ax=fig)
    mx[mx.CLAVE == 6].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='plum', label='IZTACALCO', ax=fig)
    mx[mx.CLAVE == 7].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='paleturquoise', label='IZTAPALAPA', ax=fig)
    mx[mx.CLAVE == 8].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='pink', label='LA MAGDALENA CONTRERAS', ax=fig)
    mx[mx.CLAVE == 9].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='skyblue', label='MILPA ALTA', ax=fig)
    mx[mx.CLAVE == 10].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='olive', label='ALVARO OBREGON', ax=fig)
    mx[mx.CLAVE == 11].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='chocolate', label='TLAHUAC', ax=fig)
    mx[mx.CLAVE == 12].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='peru', label='TLALPAN', ax=fig)
    mx[mx.CLAVE == 13].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='gold', label='XOCHIMILCO', ax=fig)
    mx[mx.CLAVE == 14].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='salmon', label='BENITO JUAREZ', ax=fig)
    mx[mx.CLAVE == 15].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='coral', label='CUAUHTEMOC', ax=fig)
    mx[mx.CLAVE == 16].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='darkred', label='MIGUEL HIDALGO', ax=fig)
    mx[mx.CLAVE == 17].plot(kind='scatter', x='Geo Point_1', y='Geo Point_2', color='tan', label='VENUSTIANO CARRANZA', ax=fig)
    fig.set_xlabel('LATITUD')
    fig.set_ylabel('ALTITUD')
    fig.set_title('ALCALDIA')
    plt.show()

#Funcion para visualizar las estadisticas del dataset
def dataset (cd):
    #Visualizamos los primeros 5 datos del dataset
    print(cd.head())

    #Análizamos los datos que tenemos disponibles
    print('Información del dataset:')
    print(cd.info())

    print('Descripción del dataset:')
    print(cd.describe())

    print('Distribución de las ALCALDIAS :')
    print(cd.groupby('CLAVE').size())
#Funcion que nos permite guardar nuestro modelo entrenado para poderlo usar sin tener que hacer
#que el modelo vuelva a aprender
def save_model(clf):
    joblib.dump(clf, 'KNN_model.pkl')
#ghrafic_point(cdmx)
#dataset(cdmx)
#save_model(knn)