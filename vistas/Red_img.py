# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:59:46 2021

@author: peluc
"""

from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty, BoundedNumericProperty, StringProperty
from vistas.Red_img_dos import UbicImgDos

import os

Builder.load_string("""

<UbicImg>:
    
    GridLayout:
        canvas:
            Color:
                rgba:244/255.0, 208/255.0, 63/255.0, 1
            Rectangle:
                size: self.size
                pos: self.pos
      
        Button:
            text: 'SELECCIONAR IMAGEN'
          
            font_size: 27
            height: 200
            width: 300
            pos:100,400
            background_color :140/255.,187/255.,39/255.,1
            background_normal: ""  
            on_release: 
                root.manager.current = root.show_load()
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
            text: 'SALIR'
            on_press:
                app.stop()   
            font_size: 20
            height: 50
            width: 100
            pos: 350, 80
            background_color :211/255.,84/255.,0,1
            background_normal: ""  
        
    """)
class SecondPopup(Popup):
    def __init__(self, **kwargs):
        super(SecondPopup, self).__init__(**kwargs)

    def close_me(self):
        self.dismiss()
        
class UbicImg(Screen):
    
    def show_load(self):
        content = UbicImgDos(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
#   
    def dismiss_popup(self):
        self._popup.dismiss()

    def cancel(self):
        pass
  
    def load(self,path, selection):
       print(path, selection) 


    def REGRESAR(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'screen2'
        self.manager.get_screen('screen2')    
        
