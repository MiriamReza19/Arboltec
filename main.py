
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.config import Config
from kivy.properties import StringProperty, ObjectProperty,NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen

#---vistas
from vistas.navegador import *
from vistas.find_location import *
from vistas.town_halls import *
from vistas.bt_ok import * 
from vistas.Red_img import *
from vistas.bt_verArboles import *




Builder.load_string("""
<sm>:
    id: screen_manager
    menu_screen: menu_screen
    settings_screen: settings_screen
    screenResult : screenResult
    
    StarScreen:
        name :'menu'
        manager: screen_manager
    
    MenuScreen:
#       id: menu_screen
        name: 'screen2'
        manager: screen_manager
    FoundScreen:
        id: menu_screen
 #       id: settings_screen
        name: 'loca1'
        manager: screen_manager
    TreeZone:
        name: 'zone'
        manager: screen_manager
    VerArboles:
        id: settings_screen
        name: 'TreeDes'
        manager: screen_manager  
    UbicImg:
        name:'RedScreenU'
    BTverArb:
        id:screenResult
        name:'ResRFDScreen'
        

""")

#para cancelar circulos rojos
Config.set('input','mouse','mouse,multitouch_om_demand')

#no se redimensione
Config.set('graphics','resizable', False)
#Config.set('graphics', 'width', '700')
#Config.set('graphics', 'height', '480')

#class MyApp(App):
#
#
#    def build(self):
#        Window.size=(480,700)
#        sm = ScreenManager()
#        sm.menu_screen=ObjectProperty(None)
#        sm.settings_screen=ObjectProperty(None)
#        
#        sm.add_widget(StarScreen(name='menu'))
#        sm.add_widget(MenuScreen(name='screen2'))
#        sm.add_widget(FoundScreen(name='loca1'))
#        sm.add_widget(TreeZone(name='zone'))
#        sm.add_widget(VerArboles(name='TreeDes'))#,label_text = str(FoundScreen.text)))
#        sm.add_widget(UbicImg(name='RedScreenU'))
#
#    
#
#
#        return sm


class sm(ScreenManager):
    menu_screen=ObjectProperty(None)
    settings_screen=ObjectProperty(None)
    screenResult = ObjectProperty(None)
    

    

class MyApp(App):
    
    
    def build(self):  
        Window.size=(500,700)          
        return sm()

    
if __name__ == '__main__':

    MyApp().run()
   