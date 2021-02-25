"""
Created on Fri Oct  9 17:21:36 2020

@author: miriam
"""
#from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy_garden.mapview import MapView,MapMarker
from kivy.uix.gridlayout import GridLayout

Builder.load_string("""
       
<TreeZone>:
    GridLayout:
        canvas:
            Color:
                rgba:245/255.0, 199/255.0, 116/255.0, 1
            Rectangle:
                size: self.size
                pos: self.pos
                
        Label:
            id: label1
            color: 1,1,1,1
            text:'ARBOLES POR ZONA'
            text_size:root.width,None 
            #size:root.width,root.height
            font_size:30
            bold:True
            #size.hint:1.0,0.17
            pos: 300,630 
        
        Button:
            text: 'ALVARO OBREGON'
            on_press: 
                #root.manager.current ='loca1'
               #
            font_size: 25
            height: 50
            width: 400
            pos:40, 550
            background_color :160/255.,119/255.,0/255.,1
            background_normal: "" 
            
        Button:
            text: 'MILPA ALTA'
            on_press: 
                root.manager.current ='loca1'
            font_size: 25
            height: 50
            width: 400
            pos:40, 480
            background_color :160/255.,119/255.,0/255.,1
            background_normal: "" 
        
        Button:
            text: 'MIGUEL HIDALGO'
            on_press: 
                root.manager.current ='loca1'
            font_size: 25
            height: 50
            width: 400
            pos:40, 410
            background_color :160/255.,119/255.,0/255.,1
            background_normal: "" 
       
        Button:
            text: 'TLALPAN'
            on_press: 
                root.manager.current ='loca1'
            font_size: 25
            height: 50
            width: 400
            pos:40, 340
            background_color :160/255.,119/255.,0/255.,1
            background_normal: "" 
        
        Button:
            text: 'TLAHUAC'
            on_press: 
                root.manager.current ='loca1'
            font_size: 25
            height: 50
            width: 400
            pos:40, 270
            background_color :160/255.,119/255.,0/255.,1
            background_normal: "" 
            
        Button:
            text: 'BENITO JUAREZ'
            on_press: 
                root.manager.current ='loca1'
            font_size: 25
            height: 50
            width: 400
            pos:40, 200
            background_color :160/255.,119/255.,0/255.,1
            background_normal: ""
         
        Button:
            text: 'REGRESAR'
            on_press: 
                root.REGRESAR()
            font_size: 20
            height: 50
            width: 200
            pos:250, 80
            background_color :248/255.,49/255.,6/255.,1
            background_normal: "" 
""")
##----------------------------CONECTAR BASE DE DATOS
#def connect_to_database(path) :
#    try:
#        con =- sqlite3.connect(path)
#        con.close()
#    except Exception as e:    
#        print(e)
##---------------------------- 
    
    
class TreeZone(Screen):
    
#    def __init__(self,smanager,**kwargs):
#        super(TreeZone,self).__init__()
#        self.smanager = smanager
#        
#    def create_database(self):
#        connect_to_database(self.smanager.DB_PATH)
#    
    def REGRESAR(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'screen2'
        self.manager.get_screen('screen2')  
        
#class Screen_alcal(GridLayout):
#    def __init__(self,smanager,**kwargs):
#        super(Screen_alcal,self).__init__()
#        self.smanager = smanager
#        
#    def create_database(self):
#        connect_to_database(self.smanager.DB_PATH)
#        
#    
#class DatabaseWid(GridLayout):
#    def __init__(self,smanager,**kwargs):
#        super(DatabaseWid,self).__init__()
#        self.smanager = smanager
#        
    