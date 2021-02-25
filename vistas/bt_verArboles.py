# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 14:26:32 2021

@author: peluc
"""

#from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,FadeTransition
from kivy.properties import StringProperty

Builder.load_string("""
       
<BTverArb>:
    GridLayout:
        canvas:
            Color:
                rgba:228/255.0, 138/255.0, 249/255.0, 1
               
            Rectangle:
                size: self.size
                pos: self.pos
                
        Label:
            id: label_titulo
            
            text:'RESULTADO ARBOL'
            color: 1,1,1,1
            outline_color: (0,0,0)
            outline_width: 2
            text_size:root.width,None 
            #size:root.width,root.height
            font_size:30
            bold:True
            #size.hint:1.0,0.17
            
            pos: 300,600 
            
        Label:
            
            id: label1
            color: 1,1,1,1
            text:root.label_resultado
            #text_size:root.width,None 
            background_color: (245/255, 163/255, 20/255,1)
            canvas.before:
                Color:
                    rgba:self.background_color
                Rectangle:
                    size: 300,50
                    pos:  50,430
            #size:root.width,root.height
            font_size:25
            bold:True
            #size.hint:1.0,0.17
            pos: 100,400 
            
        Label:
            id: label2
            color: 1,1,1,1
            text:root.label_resultado1
            text_size:root.width,None 
            background_color: (245/255, 163/255, 20/255,1)
            canvas.before:
                Color:
                    rgba:self.background_color
                Rectangle:
                    size: 300,50
                    pos:  50,330
            #size:root.width,root.height
            font_size:25
            bold:True
            #size.hint:1.0,0.17
            pos: 300,300 
            
        Label:
            id: label3
            color: 1,1,1,1
            text:root.label_resultado2
            text_size:root.width,None 
            background_color: (245/255, 163/255, 20/255,1)
            canvas.before:
                Color:
                    rgba:self.background_color
                Rectangle:
                    size: 300,50
                    pos:  50,230
            #size:root.width,root.height
            font_size:25
            bold:True
            #size.hint:1.0,0.17
            pos: 300,200 
            
        Button:
            text: 'REGRESAR'
            on_press: 
                root.REGRESAR()
#                root.borrar()
            height: 50
            width: 100
            pos:30, 20
            background_color :248/255.,49/255.,6/255.,1
            background_normal: "" 
            
#        Button:
#            text: 'MAPA'
#            on_press: 
#                root.manager.current ='loca1'
#            
#            font_size: 20
#            height: 50
#            width: 100
#            pos:200, 20
#            background_color :252/255.,179/255.,25/255.,1
#            background_normal: ""
            
        Button:
            text: 'MENU'
            on_press: 
                root.manager.current ='screen2'
            
            font_size: 20
            height: 50
            width: 100
            pos:370, 20
            background_color :252/255.,179/255.,25/255.,1
            background_normal: ""    
""")

class BTverArb(Screen):
    
    label_resultado = StringProperty()
    label_resultado1 = StringProperty()
    label_resultado2 = StringProperty()
  
    
    def __init__(self,**kwargs):
        super(BTverArb, self).__init__(**kwargs)  
        
        self.label_resultado=" - "
        self.label_resultado1=" - "
        self.label_resultado2=" - "
    
    def UpdateSettings(self,lbl_res):
    
       #    print(lbl_res)
           self.label_resultado=lbl_res
           
    def Update1(self,lbl_res1):
#           print(lbl_res1)
           self.label_resultado1=lbl_res1

    def Update2(self,lbl_res2):
#           print(lbl_res2)
           self.label_resultado2=lbl_res2
    
#    def  borrar(self):    
#        self.ids['label1'].text = ""    
#        self.ids['label2'].text = ""  
#        self.ids['label3'].text = ""  
        
           
    def REGRESAR(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'loca1'
        self.manager.get_screen('loca1')              