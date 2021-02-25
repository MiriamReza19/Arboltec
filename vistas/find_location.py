"""
Created on Fri Oct  9 17:21:36 2020

@author: miriam
"""
#from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

#from kivy.uix.label import Label
from kivy.properties import NumericProperty
#from kivy.garden.mapview import MapMarker
#from kivy.uix.screenmanager import SlideTransition
from kivy.base import runTouchApp
from kivy.properties import StringProperty, ObjectProperty
from kivy_garden.mapview import MapView,MapMarker
from algoritmo_knn.Modelo_KNN import prediction


Builder.load_string("""

<Toolbar@GridLayout>:
    size_hint_y: 0.20
    height: '48dp'
    padding: '4dp'
    spacing: '4dp'
    canvas:
        Color:
            rgba: 0,0,0,1
        Rectangle:
            pos: 0,650
            size:self.size
<FoundScreen>:
    id: screen_map
    GridLayout:
        id:pantalla
        canvas:
            Color:
                rgba:133/255.0, 229/255.0, 250/255.0, 1
            Rectangle:
                size: self.size
                pos: self.pos
        
        MapView:
            id: mapview
            lat: 19.42847
            lon: -99.12766
         
            zoom: 11
            double_tap_zoom: True
            on_zoom:
                self.zoom = 10 if self.zoom <10 else self.zoom
            on_lat:
                print('lat',self.lat)
            on_lon:
                print('lon',self.lon)
            
            pos:0,180
            
            height : dp(500)
            width: dp(500) 
#          
        
                
                
        Toolbar: 
            
#            Button:
#                height:30
#                text: "-"
#                pos:0,250
#                on_release: root.men_zoom()   
            
            Button:
                height:30
                text: "Azcapotzalco"
                pos:0,150
                on_release: mapview.center_on(19.48698,  -99.18594)             
                
            Button:
                height:30
                text: "Coyoacan"
                pos:100,150
                on_release: mapview.center_on(19.34670,  -99.16174)
                
            Button:
                height:30
                text: "Magdalena C."
                pos:200,150
                on_release: mapview.center_on(19.33212,  -99.21118)
            
            Button:
                height:30
                text: "Tlahuac"
                pos:300,150
                on_release: mapview.center_on(19.28689,  -99.00507)
         
            Button:
                height:30
                text: "Iztacalco"
                pos:400,150
                on_release: mapview.center_on(19.39528,  -99.09778)        
            Button:
                height:30
                text: "Miguel H."
                pos:0,120
                on_release: mapview.center_on(19.4182,  -99.2010)
        
                
            Button:
                height:30
                text: "Xochimilco"
                pos:100,120
                on_release: mapview.center_on(19.25465, -99.10356)
            
            Button:
                height:30
                text: "Venustiano C"
                pos:200,120
                on_release: mapview.center_on(19.44361, -99.10499)        
                
            Button:
                height:30
                text: "Tlalpan"
                pos:300,120
                on_release: mapview.center_on(19.29513, -99.16206) 
            Button:
                height:30
                text: "Cuajimalpa"
                pos:400,120
                on_release: mapview.center_on(19.36920, -99.29089)
            Button:
                height:30
                text: "Iztapalapa"
                pos:0,90
                on_release: mapview.center_on(19.35529, -99.06224) 
            Button:
                height:30
                text: "MilpaAlta"
                pos:100,90
                on_release: mapview.center_on(19.11260, -99.01190) 
            Button:
                height:30
                text: "Benito J."
                pos:200,90
                on_release: mapview.center_on(19.37270, -99.15640) 
            Button:
                height:30
                text: "Gustavo A.M."
                pos:300,90
                on_release: mapview.center_on(19.49392, -99.11075) 
            Button:
                height:30
                text: "Cuahutemoc"
                pos:400,90
                on_release: mapview.center_on(19.44506, -99.14612) 
        
            Button:
                height:30
                text: "Alvaro O."
                pos:200,60
                on_release: mapview.center_on(19.35867, -99.20329)
        Toolbar:
            
            width: 800
            Label:
                pos:300,630
                text: "Altitude: {}".format(mapview.lon)
                
            Label:
                pos:80,630
                text: "Latitude: {}".format(mapview.lat)    
        Button:
            text: 'Ok'
            on_press: 
                root.manager.current ='TreeDes'
                root.Coordenadas()

                
            font_size: 20
            height: 50
            width: 200
            pos:250, 13
            background_color :64/255.,218/255.,41/255.,1
            background_normal: "" 
         
        Button:
            text: 'REGRESAR'
            on_press: 
                root.REGRESAR()
            font_size: 20
            height: 50
            width: 200
            pos:30, 13
            background_color :248/255.,49/255.,6/255.,1
            background_normal: "" 
            
       
""")

class FoundScreen(Screen):

 
    T = StringProperty()
    OB = StringProperty()
    
    label1=StringProperty()

    
    def __init__(self,**kwargs):
        super(FoundScreen, self).__init__(**kwargs)  
        self.label1="MIriam"
      
        
        self.T = ""
#    def men_zoom(self)    :
#        zoom = self.zoom
#        zoom -= 1
    def Coordenadas(self,**kwargs):
      try:  
        alcal1 ="Coyoacán"
        alcal2 ="Miguel HIdalgo"
        alcal3 = "Magdalena contreras"
        alcal4 ="Tlahuac"
        alcal5 ="Azcapotzalco"
        alcal6 = "Iztacalco"
        alcal7 = "Alvaro Obregon"
        alcal8 = "Xochimilco"
        alcal9 = "Venustiano Carranza"
        alcal10= "Tlalpan"
        alcal11= "Cuajimalpa"
        alcal12= "Iztapalapa"
        alcal13= "MilpaAlta"
        alcal14= "Benito Juarez"
        alcal15= "Gustavo A.Madero"
        alcal16= "Cuahutemoc"
        
    
        latit= self.ids['mapview'].lat
        alti= self.ids['mapview'].lon
        R = prediction([latit,alti])
        R1 = str(R[0])
        print(R1)
#        
#        
        if R1 == ('15') :
            lbl1 = self.T + alcal16
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)
            
        elif R1 == ('3') :
            lbl1 = self.T + alcal1
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)
        elif R1 == ('16') :
            lbl1 = self.T + alcal2
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)
        elif R1 == ('8') :
            lbl1 = self.T + alcal3
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)
        elif R1 == ('11') :
            lbl1 = self.T + alcal4
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)  
        elif R1 == ('2') :
            lbl1 = self.T + alcal5
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)
        elif R1 == ('6') :
            lbl1 = self.T + alcal6
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)  
        elif R1 == ('10') :
            lbl1 = self.T + alcal7
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1) 
        elif R1 == ('13') :
            lbl1 = self.T + alcal8
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)
        elif R1 == ('17') :
            lbl1 = self.T + alcal9
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)
        elif R1 == ('12') :
            lbl1 = self.T + alcal10
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1) 
        elif R1 == ('4') :
            lbl1 = self.T + alcal11
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)
        elif R1 == ('7') :
            lbl1 = self.T + alcal12
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)
        elif R1 == ('9') :
            lbl1 = self.T + alcal13
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)  
        elif R1 == ('14') :
            lbl1 = self.T + alcal14
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)  
        elif R1 == ('5') :
            lbl1 = self.T + alcal15
            chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
            chg.UpdateSettings(lbl1)  
        
        else:
            print("No valido ALCALDIA")
      except:
          pass
    
        
#    def change_text(self):          
##        lbl1=self.label1 + " and Marco"
#        lbl1 = self.label_alcal
#        
#        chg = self.manager.settings_screen  #<<<<<<<<<<<<<<
#        chg.UpdateSettings(lbl1)
        
    def REGRESAR(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'screen2'
        self.manager.get_screen('screen2')
        
