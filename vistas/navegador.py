#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:21:36 2020

@author: miriam
"""
#from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import Screen,FadeTransition
#from kivy.core.window import Window #cambiar fondo de la palicacionn 
#from kivy.uix.image import Image
#from kivy.graphics import Color
#from kivy.uix.label import Label
#from kivy.uix.button import Button
#from kivy.properties import ObjectProperty()
#from find_location.py import *
import os
import sqlite3
Builder.load_string("""
              
<StarScreen>:

    GridLayout:
        canvas:
            Color:
                rgba:255/255.0, 227/255.0, 135/255.0, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            source:'arbol.png'
            size_hint_y : 0.20
            size_hint_x: None
            height : dp(400)
            width: self.parent.width
            #height: self.parent.width
            pos:10, 270
            
        Button:
            text: 'INICIAR'
            on_press: 
                
                root.manager.current ='screen2'
                
            background_color: [ 71/255.,196/255.,8/255.,1] 
            background_normal: ""
            height: 50
            width: 400
            pos:50, 180
                
<MenuScreen>:
    GridLayout:
        canvas:
            Color:
                rgba:255/255.0, 227/255.0, 135/255.0, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Button:
            text: 'ENCONTRAR UBICACION'
            on_press: 
                root.manager.current ='loca1'
                root.manager.transition.direction='left'
            font_size: 30
            height: 100
            width: 400
            pos:50, 550
            background_color :64/255.,218/255.,41/255.,1
            background_normal: ""
            
        Button:
            text: 'ARBOLES POR ZONA'
            on_press: 
                root.manager.current ='zone'
                root.manager.transition.direction='left'
            font_size: 30
            height: 100
            width: 400
            pos:50, 400
            background_color :64/255.,218/255.,41/255.,1
            background_normal: ""
            
        Button:
            text: 'IDENTIFICAR ARBOL'
            on_press: 
                root.manager.current ='RedScreenU'
                root.manager.transition.direction='left'
            font_size: 30
            height: 100
            width: 400
            pos:50, 250
            background_color :64/255.,218/255.,41/255.,1
            background_normal: ""
        
        Button:
            text: 'REGRESAR'
            on_press: 
                root.REGRESAR()
            font_size: 20
            height: 50
            width: 200
            pos:30, 80
            background_color :248/255.,49/255.,6/255.,1
            background_normal: ""  
       
        Button:
            text: 'Salir'
            on_press:
                app.stop()   
            font_size: 20
            height: 50
            width: 100
            pos: 350, 80
            background_color :211/255.,84/255.,0,1
            background_normal: ""  
          
""")

                
class StarScreen(Screen):
  
    def screen1 (self):
    #   super.__init__()
     pass
        
        
class MenuScreen(Screen):
    
    
   
    def screen2 (self):
    #   super.__init__()
      pass
    
    def REGRESAR(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'menu'
        self.manager.get_screen('menu')    

                   