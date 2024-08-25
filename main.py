from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.toast.kivytoast.kivytoast import toast
import webbrowser

kv='''

Manager:
    Fir:
    Sec:
               
<Fir>:
    MDBottomNavigation:
        panel_color:0,1,0,1
        text_color_active:1,0,0,1
        text_color_normal:0,0,1,1
        MDBottomNavigationItem:
            name:'s1'
            icon:'home'
            text:'HOME'
            Carousel:
                direction:'bottom'
                MDLabel:
                    text:'HAR HAR MAHADEV'
                    bold:True
                    halign:'center'
                    font_size:'50sp'
                    text_color:0,0,1,1
                    font_size:'50sp'
                   
        MDBottomNavigationItem:
            name:'s2'   
            icon:'android'              
            text:'THEME CHANGER'         
            MDSwitch:
                id:sw1
                on_active:app.th()           
                
            
                                                     
                    
                    
                    
                    

    MDTopAppBar:
        id:m1
        title:'HAR HAR MAHADEV'
        pos_hint:{"top":1}
        md_bg_color:0,1,0,1
        left_action_items:[['youtube',lambda x: app.pr()]]








'''











class Fir(Screen):
    pass
    
    
class Sec(Screen):
    pass
    
    
class Manager(ScreenManager):
    pass


class Demo(MDApp):
    def build(self):
        self.u=Builder.load_string(kv)
        return self.u
    def pr(self):
        webbrowser.open('https://youtube.com/shorts/kKQv_wpl4vM?si=stHFkYJBjMfDI4pd')        
    def th(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"                 
                       
        
        
        

Demo().run()
