"""
Created on Fri Oct  9 17:21:36 2020

@author: miriam
"""
#from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, FadeTransition
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
#from kivy.garden.mapview import MapMarker
#from kivy.uix.screenmanager import SlideTransition
from kivy.base import runTouchApp
from kivy.properties import StringProperty, ObjectProperty
from kivy_garden.mapview import MapView,MapMarker
from algoritmo_RFD.RFD_model import RFDprediction
from kivy.uix.label import Label

Builder.load_string("""                  

<VerArboles>:
    GridLayout:
        id:pantalla1
        canvas:
            Color:
                rgba:133/255.0, 229/255.0, 250/255.0, 1
            Rectangle:
                size: self.size
                pos: self.pos
        Label:
           
            color: 1,1,1,1
            text: 'Alcaldia:'
           #text_size:root.width,None 
           #size:root.width,root.height
            font_size:30
            bold:True
           #size.hint:1.0,0.17
            pos: 50,500 
            
        Label:
            id: label_alcal
            color: 1,1,1,1
            text:root.label3
           #text_size:root.width,None 
            size:250,50
            font_size:25
            bold:True
            canvas.before:
                Color:
                    rgba:  37/255.,99/255.,237/255.,1
                Rectangle:
                    pos: self.pos
                    size: self.size
            
            pos: 200,530 
                      
        Label:
           
            color: 1,1,1,1
            text: 'Suelo:'
           #text_size:root.width,None 
           #size:root.width,root.height
            font_size:30
            bold:True
           #size.hint:1.0,0.17
            pos: 50,400      
        
        Spinner:
            id:spin_suelo
            size_hint: None, None
            size: 250, 50
            pos: 200,430
            text: 'SUELO'
            background_color :37/255.,99/255.,237/255.,1
            values: 'ADAPTABLE', 'ARENOSO', 'CALIZO', 'LIMOSO', 'TIERRA NEGRA', 'ARCILLOSO', 'PEDREGOSO', 'DE TURBA', 'SALINO', 'ACIDO', 'ROCOSO'
            on_text:
                
                print("The spinner {} has text {}".format(self, self.text))
 
            
        Label:
            id: label3
            color: 1,1,1,1
            text: 'Clima:'
           #text_size:root.width,None 
           #size:root.width,root.height
            font_size:30
            bold:True
           #size.hint:1.0,0.17
            pos: 50,300  
       
        Spinner:
            id:spin_clima
            size_hint: None, None
            size: 250, 50
            pos: 200,330
            text: 'CLIMA'
            background_color :37/255.,99/255.,237/255.,1
            values: 'TROPICAL', 'SECO', 'TEMPLADO', 'CONTINENTAL', 'ALTA MONTAÑA', 'SELVA TROPICAL', 'TROPICAL MONZONICO', 'ADAPTABLE', 'ARIDO', 'SEMIARIDO', 'MEDITERRANEO', 'TEMPLADO SUBHUMEDO', 'CALIDO'
            on_text:

                print("The spinner {} has text {}".format(self, self.text))
      
                
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
            text: 'VER ARBOLES'
            on_press: 
                root.RFD_result()
                root.manager.current ='ResRFDScreen'
            
            font_size: 20
            height: 50
            width: 200
            pos:250, 80
            background_color :252/255.,179/255.,25/255.,1
            background_normal: ""  
  
            
""")
class VerArboles(Screen):


    label3=StringProperty()
    total =StringProperty()
    total1 =StringProperty()     
    total2 =StringProperty() 
#    label3 =StringProperty()
   
    def __init__(self,**kwargs):
        super(VerArboles, self).__init__(**kwargs)  
        #some default texts
        self.label3="Nothing"
        self.total=" "
        self.total1=" "
        self.tota2=" "
    
    def UpdateSettings(self,lbl1):
        
        print(lbl1)
        self.label3=lbl1
       
    def RFD_result(self,**kwargs):
     #imprimir el texto del label alcaldia  
     try:
       x =self.ids.label_alcal.text
       print(x)


       if x == "Coyoacán":
          x = 3
       elif x == "Miguel HIdalgo":
          x = 16
       elif x == "Magdalena contreras":
          x = 8
       elif x == "Tlahuac": 
          x = 11
       elif x == "Azcapotzalco":
          x = 2
       elif x == "Iztacalco":
          x = 6
       elif x == "Alvaro Obregon":
          x = 10 
       elif x ==  "Xochimilco":
          x = 13
       elif x == "Venustiano Carranza":
          x = 17
       elif x ==  "Tlalpan":
          x = 12
       elif x == "Cuajimalpa":
          x = 4
       elif x ==  "Iztapalapa":
          x = 7
       elif x == "MilpaAlta" :
          x = 9
       elif x == "Benito Juarez":
          x = 14
       elif x == "Gustavo A.Madero":
          x = 5
       elif x == "Cuahutemoc" :
          x = 15
     
         
    #imprimir el texto del spinner clima 
     
      
       x1 = self.ids.spin_clima.text  
       if x1 == "TROPICAL":
           x1 = 1200
           
       elif x1 == "SECO":
           x1 = 1201
          
       elif x1 == "TEMPLADO":
           x1 = 1202
           
       elif x1 == "CONTINENTAL":
           x1 = 1203
           
       elif x1 == "ALTA MONTAÑA":
           x1 = 1205
             
       elif x1 == "SELVA TROPICAL":
           x1 = 1206
             
       elif x1 == "TROPICAL MONZONICO":
           x1 = 1207
           
       elif x1 == "ADAPTABLE":
           x1 = 1208
          
       elif x1 == "ARIDO":
           x1 = 1209
           
       elif x1 == "SEMIARIDO":
           x1 = 1210
          
#       elif x1 == "OCEANICO":
#           x1 = 1212
#           print(x1)
       elif x1 == "TEMPLADO SUBHUMEDO":
           x1 = 1213
          
       elif x1 == "SUBTROPICAL":
           x1 = 1215
           
       elif x1 == "TEMPLADO":
           x1 = 1202
           
   
       #print(x1)
    #imprimir el texto del spinner suelo 
     
       x2 = self.ids.spin_suelo.text
       print(x2)
       if x2 == "ADAPTABLE":
           x2 = 1000
           print(x2)
       elif x2 == "ARENOSO":
           x2 = 1001
           print(x2)
       elif x2 == "CALIZO":
           x2 = 1002
           print(x2)
       elif x2 == "LIMOSO":
           x2 = 1003
           print(x2)
       elif x2 == "TIERRA NEGRA":
           x2 = 1004  
           print(x2)
       elif x2 == "ARCILLOSO":
           x2 = 1005
           print(x2)
       elif x2 == "PEDREGOSO":
           x2 = 1006
           print(x2)
       elif x2 == "DE TURBA":
           x2 = 1007
           print(x2)
       elif x2 == "SALINO":
           x2 = 1008
           print(x2)
       elif x2 == "ACIDO":
           x2 = 1006
           print(x2)

   
       
       t = [x,x2,x1]
           
       t2 = RFDprediction(t)
       
       t1= str(t2)
       print(t1)
       
       if t1 == ("['20,50']"):
           Abl = "Acacia negra"
           lbl_res = self.total + Abl            
           chg = self.manager.screenResult  #<<<<<<<<<<<<<<
           chg.UpdateSettings(lbl_res) 
      # print(lbl_res)
           Abl1 = "Olivo"
           lbl_res1 = self.total1 + Abl1 
           chg.Update1(lbl_res1)
            
       elif t1 == ("['21']"):
               Abl = "Acacia Azul"
               lbl_res = self.total + Abl 
               print(lbl_res)
               chg = self.manager.screenResult
               chg.UpdateSettings(lbl_res)  
#               
           
       elif t1 == ("['22,61']"):
               Abl = "Arbol Orquidea"
               lbl_res = self.total + Abl
               chg = self.manager.screenResult  #<<<<<<<<<<<<<< 
               chg.UpdateSettings(lbl_res) 
               Abl1 = "Sicomoro"
               lbl_res1 = self.total1 + Abl1 
               chg1 = self.manager.screenResult
               chg1.Update1(lbl_res1)
       
       elif t1 == ("['23']"):
               Abl = "Ciruelo"
               lbl_res = self.total + Abl  
               print(lbl_res)
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
       
       elif t1 == ("['24']"):
               Abl = "Ebano"
               lbl_res = self.total + Abl   
               print(lbl_res)
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
      
       elif t1 == ("['25']"):
               Abl = "Ebano"
               lbl_res = self.total + Abl  
               print(lbl_res)
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)  
               
       elif t1 == ("['26']"):
               Abl = "Jacaranda"
               lbl_res = self.total + Abl 
               print(lbl_res)
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
               
       elif t1 == ("['27']"):
               Abl = "Limonero"
               lbl_res = self.total + Abl 
               print(lbl_res)
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
               
       elif t1 == ("['28']"):
               Abl = "Mangolia"
               lbl_res = self.total + Abl 
               print(lbl_res)
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
       
       elif t1 == ("['29']"):
               Abl = "Mimosa"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
               
       elif t1 == ("['30,40,43']"):
               Abl = "Acacia Azul"
               lbl_res = self.total + Abl 
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
               
               Abl1 = "Encino siempre verde"
               lbl_res1 = self.total1 + Abl1
               chg1 = self.manager.screenResult
               chg1.Update1(lbl_res1)
               
               Abl2 = "Grevilla"
               lbl_res2 = self.total2 + Abl2
               chg2 = self.manager.screenResult
               chg2.Update2(lbl_res2)
               
               
       elif t1 == ("['31']"):
               Abl = "Palo Dulce"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
       
       elif t1 == ("['32']"):
               Abl = "Piru de Brasil"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
               
       elif t1 == ("['33']"):
               Abl = "Trueno"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)  
               
       elif t1 == ("['34']"):
               Abl = "Ahuehuete"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)   
               
       elif t1 == ("['35']"):
               Abl = "Ahuejote"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)         
               
       elif t1 == ("['36']"):
               Abl = "Aile"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)         
       
       elif t1 == ("['37']"):
               Abl = "Trueno"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
       
       elif t1 == ("['38']"):
               Abl = "Capulin"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)  
        
       elif t1 == ("['39']"):
               Abl = "Chabacano"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)  
               
       elif t1 == ("['40']"):
               Abl = "Encino siempre verde"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)         
       
       elif t1 == ("['41']"):
               Abl = "Encino"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
               
       elif t1 == ("['42']"):
               Abl = "Fresno"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)        
       
       elif t1 == ("['44']"):
               Abl = "Guayabo"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)    
               
       elif t1 == ("['45']"):
               Abl = "Huizache"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)   
               
       elif t1 == ("['46']"):
               Abl = "Liquidambar"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)        
       
       elif t1 == ("['47']"):
               Abl = "Manzano"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
       
       elif t1 == ("['48']"):
               Abl = "Mezquite"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)  
       
       elif t1 == ("['49']"):
               Abl = "Negundo"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
    
       
       elif t1 == ("['51']"):
               Abl = "Palma Abanico"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
       
       elif t1 == ("['52']"):
               Abl = "Palma datilera"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)        
    
       elif t1 == ("['53']"):
               Abl = "Palo de rosa"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
               
       elif t1 == ("['54']"):
               Abl = "Peral"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)        
       elif t1 == ("['55']"):
               Abl = "Pino alepo"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
    
       elif t1 == ("['56']"):
               Abl = "Pino Ayacahuite"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
    
       elif t1 == ("['57']"):
               Abl = "Pino Azul "
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
    
       elif t1 == ("['58']"):
               Abl = "Pino Piñonero"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
    
       elif t1 == ("['59']"):
               Abl = "Piru común"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)
               
       elif t1 == ("['60']"):
               Abl = "Sauce"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
               
#       elif t1 == (['61']):
#               Abl = "Sicomoro"
#               lbl_res = self.total + Abl            
#               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
#               chg.UpdateSettings(lbl_res)
       
       elif t1 == ("['62']"):
               Abl = "Tecojote"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
               
       elif t1 == ("['63']"):
               Abl = "Tepozan"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)        
       
       elif t1 == ("['64']"):
               Abl = "Cazahuate"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)  
               
       elif t1 == ("['65']"):
               Abl = "Encino quiebra hacha"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)   
               
       elif t1 == ("['66']"):
               Abl = "Ayacahuite"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)        
               
       elif t1 == ("['67']"):
               Abl = "Pino llorón"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)   
       
       elif t1 == ("['69,70']"):
               Abl = "Colorin"
               lbl_res = self.total + Abl   
               
               Abl1 = "Palma Caribeña"
               lbl_res1 = self.total + Abl1
               
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
               chg1 = self.manager.screenResult
               chg1.Update1(lbl_res1)
       elif t1 == ("['29,51']"):
               Abl = "Mimosa"
               lbl_res = self.total + Abl   
               
               Abl1 = "Palma abanico"
               lbl_res1 = self.total + Abl1
               
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)  
               chg1 = self.manager.screenResult
               chg1.Update1(lbl_res1)
               
       elif t1 == ("['68']"):
               Abl = "Cedro Blanco"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)  
               
       elif t1 == ("['69']"):
               Abl = "Colorin"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
               
       elif t1 == ("['70']"):
               Abl = "Palma Caribeña"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res)   
       elif t1 == ("['71']"):
               Abl = "Izote"
               lbl_res = self.total + Abl            
               chg = self.manager.screenResult  #<<<<<<<<<<<<<<
               chg.UpdateSettings(lbl_res) 
       else:
           Abl = "  NO HAY REGISTRO "
           lbl_res = self.total + Abl            
           chg = self.manager.screenResult  #<<<<<<<<<<<<<<
           chg.UpdateSettings(lbl_res)    
           
           
           
#     
#     except:
#         pass
     except ValueError:
          popup = Popup(title='Test popup',content=Label(text='FALTA DE INFORMACION'),
                   size_hint=(None, None), size=(400, 400))
      
          popup.open()
         

    
       
#       popup = Popup(title='Test popup',content=Label(text='Hello world'),
#                   size_hint=(None, None), size=(400, 400))
#       if total == 'None':
#           
#           popup.open()
#           
#           print(t1)
       
       
    def REGRESAR(self):
        self.manager.transition = FadeTransition()
        self.manager.current = 'loca1'
        self.manager.get_screen('loca1')     
        


                       