# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:47:00 2021

@author: peluc
"""

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, BoundedNumericProperty, StringProperty
from kivy.uix.popup import Popup
from Red_neuronal.Predecir import predict
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import os

Builder.load_string("""
#:import Factory kivy.factory.Factory
<UbicImgDos>:
    
    id:ubic
    BoxLayout:
        id:BOX1
        size: root.size
        pos: root.pos
        orientation: "vertical"
        
   #     padding:50 
    #    spacing:20
    
        TextInput:
            id:texto_im
            size_hint: (.9, None)
            height: 30
            pos: root.pos
            text:root.PT
                
        Image:
            id:my_image
            source: ""
            
        FileChooserIconView:
            id:filechooser
            on_selection: ubic.select(filechooser.selection)
     
       
        BoxLayout:
            
            size_hint_y:None
            height:30
           
            Button:
                text:"CANCELAR"
                on_release: root.cancel()
            
            Button:
                text:"OK"
                
                on_release:
                  
                    root.put_text()
                   
 

<SecondPopup>:
    id:second_popup
    title:"RESULTADO iMAGEN"
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: second_label
 #           text: root.put_text()
        Button:
            text: 'no se'
#            on_release: 
#                root.SecondPopup()
        Button:
            text: 'CERRAR'
            on_release: 
                root.close_me()            
    """)
                  
class UbicImgDos(FloatLayout):
    
 
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    RN =StringProperty(None)
   # SI = StringProperty(None)
    PT2= StringProperty()
    PT = StringProperty()
    def __init__(self,**kwargs):
        super(UbicImgDos, self).__init__(**kwargs)  
        

        self.RN =""

        self.PT ="Ruta del archivo"
    def select(self,filename):
        global save_img
        global PT
        try:
             self.ids.my_image.source = filename[0]
             save_img = filename[0]
             self.PT = str(save_img)
        except:
            pass


             

         
    def put_text (self,**args):
     try:       
#             self.RN= predict(self.PT)
#             x = str(self.RN)
#             print("Mi intento",x)
             pt2 =self.PT
#             print(pt2)
             RN = predict(pt2)
#             print(RN)
             
             if RN == 0:
                 X=("Acacia azul")
             elif RN == 1:
                 X=("Acacia Negra")
             elif RN == 2:
                 X=("Ahuehuete")
             elif RN == 3:
                 X=("Ahuejote")
             elif RN == 4:
                 X=(" Aile")
             elif RN == 5:
                 X=("Arbol Orquidea")
             elif RN == 6:
                 X=("Astronomica")
             elif RN == 7:
                 X=("Ayacahuite")
             elif RN == 8:
                 X=("Capulin")
             elif RN == 9:
                 X=(" Cazahuate")
             elif RN == 10:
                 X=("Cedro blanco")
                 
                 
             #content = Popup (Label(text=X),Button)
             popup = Popup(title="NOMBRE ARBOL",
               content=Label(text=X),
#               content =content ,
               size=(100, 100),
               size_hint=(0.3, 0.3),
               auto_dismiss=True)
             popup.open()
     except  FileNotFoundError:
             popup = Popup(title='Test popup',content=Label(text='Selecciona una imagen'),
                   size_hint=(None, None), size=(400, 400))
      
             popup.open()
       

        
        
    