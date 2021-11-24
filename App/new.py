from kivy.app import App
import asyncio
pt=
webadd=
threshold=0
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib
import matplotlib.pyplot as plt
from math import sin
from kivy.garden.graph import Graph, MeshLinePlot
from kivy_garden.graph import Graph, LinePlot
import matplotlib.animation as animation
from kivy.core.window import Window
import matplotlib.pyplot as p
from kivy.uix.image import Image,AsyncImage
from pdf2image import convert_from_bytes
import io
import time
import threading
import pymysql.cursors
from kivy.core.image import Image as CoreImage
import tempfile
import os
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.clock import Clock
from kivy.garden.graph import LinePlot
from threading import Thread
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
di=[]
import pickle
dire=tempfile.mkdtemp()
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.app import MDApp
from matplotlib.widgets import Slider
import asynckivy as ak
def color(c):
        if int(c)>threshold:
            return 'r'
        else:
            return 'g'
b="""
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import MeshLinePlot kivy.garden.graph.MeshLinePlot
<ScreenManager>:
    
    transition: FadeTransition()
    LOGIN:
    SIGN:
        
    GRAPH:
    BILL:
    

<LOGIN>:
    user:user
    password:password
    name: 'li'
    MDCard:
        id: mm
        size_hint: None, None
        size: 300, 400
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            id: welcome_label
            text: "WELCOME"
            font_size: 40
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        MDTextFieldRound:
            id: user
            hint_text: "username"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}

        MDTextFieldRound:
            id: password
            hint_text: "password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True

        MDRoundFlatButton:
            text: "LOG IN"
            font_size: 12
            pos_hint: {"center_x": 0.5}
            on_press: app.logger()
            on_release:root.sho(root.ids.user.text,root.ids.password.text)
        

        MDRoundFlatButton:
            text: "CLEAR"
            font_size: 12
            pos_hint: {"center_x": 0.5} 
            on_press: app.clear()           
        Widget:
            size_hint_y: None
            height: 10
<SIGN>:
    i:noc
    name: 'SI'
    MDCard:
        size_hint: None, None
        size: 300, 600
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 25
        spacing: 25
        orientation: 'vertical'

        MDLabel:
            id: welcome_label
            text: "WELCOME"
            font_size: 40
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15

        MDTextFieldRound:
            id: user
            hint_text: "user id"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
        MDTextFieldRound:
            id: pno
            hint_text: "Phone Number"
            icon_right: "phone"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
        MDTextFieldRound:
            id: nop
            hint_text: "Number of People"
            icon_right: "account"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
        MDTextFieldRound:
            id: noc
            hint_text: "CONNECTION ID"
            icon_right: "connect"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
        MDTextFieldRound:
            id: nocs
            hint_text: "Names of Connections"
            icon_right: "android"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}


        MDTextFieldRound:
            id: password
            hint_text: "password"
            icon_right: "eye-off"
            size_hint_x: None
            width: 200
            font_size: 18
            pos_hint: {"center_x": 0.5}
            password: True

        MDRoundFlatButton:
            text: "SIGN UP"
            font_size: 12
            pos_hint: {"center_x": 0.5}
            on_press: app.signup()

        MDRoundFlatButton:
            text: "BACK"
            font_size: 12
            pos_hint: {"center_x": 0.5} 
            on_press: app.login()           

        Widget:
            size_hint_y: None
            height: 10
<GRAPH>:
    usr:''
    pss:''
    name: 'grap'
    
    BoxLayout:
        id:gr

    BoxLayout:
        id: but1
        size_hint :(.25, .05)
        
        Button:
            text:"back"
            
            on_press:app.root.current='SI'
    BoxLayout:
        id: but3
        size_hint :(.25, .05)
        pos_hint :{'x':.5, 'y':0}
        Button:
            text:"Stop"
            
            on_press:root.stop()
    BoxLayout:
        id: but2
        size_hint :(.25, .05)
        pos_hint :{"right":1}
        Button:
            text:"bill"
            
            on_press:app.root.current='bil'
    BoxLayout:
        id: but4
        size_hint :(.25, .05)
        pos_hint :{'x':.25, 'y':0}
        Button:
            text:"start"
            
            on_press:root.start()
    

<BILL>:
    name:'bil'
    background_color: 1, 1, 1, 1
    Button:
        text:"Graph"
        size_hint :(.25, .1)
        pos_hint :{"bottom":1}
        on_press:app.root.current='grap'

    


"""


class LOGIN(Screen):
    def sho(self,user,password):
        if user:
            app=TestApp.get_running_app()
            p=app.root.get_screen('grap').ids
            
    
        
class SIGN(Screen):
    i=ObjectProperty(None)
class GRAPH(Screen):
    
    def __init__(self,**kwargs):
        Window.clearcolor=(0,0,0,1)
        super(GRAPH, self).__init__(**kwargs)          
        self.layout = BoxLayout(orientation ='vertical',size_hint=[1,.95],pos_hint={'top':1})
        app=TestApp.get_running_app()
        Clock.schedule_interval(self.foo, 5)
        
    def start(self):
        sm.current='grap'
        print("started")
        Clock.schedule_interval(self.foo, 5)
    def stop(self):
        print("Paused")
        Clock.unschedule(self.foo)
        self.ids.gr.clear_widgets()
        self.layout.clear_widgets()
        self.plot()

    
        
    def plot(self):
        
        db=pymysql.connect(host='0.tcp.ap.ngrok.io',
                                            port=pt,
                                            user='root',
                                            password='',
                                            database='')
        try:
            tb_name=pickle.load( open( "lis.pkl", "rb" ) )
        except:
            tb_name='sjms'
        
        c=db.cursor()
        print(tb_name)
        sq="SELECT * FROM new_table WHERE cid = %s"

        
        try:
            print("yes")
            c.execute(sq,tb_name)
            print("no")
            out=c.fetchall()

            out=[(k[2],sum(list(k[3:]))) for k in out ]
            
            up=float(0)
            x,y=[],[]
            for i,j in out:
                if i in x:
                    y[x.myindex(i)]=y[x.myindex(i)]+j
                else:
                    print("here")
                    
                    
                    
                    x.append(i)
                    y.append(j)
                    up=j

            sq="UPDATE signup SET Volume={}  WHERE idd=%s".format(up)
            print(type(up),type(tb_name))
            c.execute(sq,(tb_name))
            db.commit()
            
            
            self.fig, self.ax = plt.subplots()
            
            self.ax.set_facecolor('pink')
            print("sdad")
            c=['r','g']
            plt.plot(x,[threshold]*(len(x)),linestyle='dotted')
            plt.plot_date(x, y,color='b', linestyle = '-')
            plt.tight_layout()
            plt.ylabel("VOLUME")
            plt.xlabel("TIME")
            self.fig.patch.set_facecolor('xkcd:mint green')
            self.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))
            self.ids.gr.add_widget(self.layout)
            ax_slide=plt.axes([0.15,0.97,0.65,0.03])
            self.slid=Slider(ax_slide, "ZOOM", matplotlib.dates.date2num(x[0]), matplotlib.dates.date2num(x[len(x)-1]))
            self.slid.on_changed(self.update)
        except Exception as e: 
            print(repr(e))
            
    
        
        

        
    

    def update(self,val):
        val=matplotlib.dates.num2date(self.slid.val)
        print("val:",val)
        
        self.ax.set_xlim(val)
        self.layout.clear_widgets()
        self.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        
    def foo(self,instance):
        self.ids.gr.clear_widgets()
        self.layout.clear_widgets()
    
        try:    
            self.fig.close()
        except:
            pass
        self.plot()
        
    


    
class BILL(Screen):
    def __init__(self,**kwargs):
        Window.clearcolor=(1,1,1,1)
        super(BILL, self).__init__(**kwargs)          
        self.layout =ModalView(
            size_hint=(0.4, 0.8),
            overlay_color=(0, 0, 0, 0),
        )
        self.bill()
    def bill(self):
        Window.clearcolor = (1,1,1,1)
        
        from reportlab.pdfgen import canvas
        self.c = canvas.Canvas("invoice.pdf",pagesize=(200,250),bottomup=0)
        self.c.translate(10,40)
        self.c.scale(1,-1)
        # c.drawImage("logo.jpg",0,0,width=50,height=30)
        self.c.scale(1,-1)
        self.c.translate(-10,-40)
        self.c.setFont("Helvetica-Bold",10)
        self.c.drawCentredString(100,20,"WATER INDUSTRY")
        self.c.line(45,22,155,22)
        self.c.setFont("Helvetica-Bold",5)
        self.c.drawCentredString(100,30,"Block No. 101, Triveni Apartments, Pitam Pura,")
        self.c.drawCentredString(100,35,"New Delhi - 110034, India")
        self.c.setFont("Helvetica-Bold",6)
        self.c.drawCentredString(100,42,"GSTIN : 07AABCS1429B1Z")
        self.c.line(5,45,195,45)
        self.c.setFont("Courier-Bold",8)
        self.c.drawCentredString(100,55,"WATERBILL")
        self.c.roundRect(15,63,170,40,10,stroke=1,fill=0)
        self.c.setFont("Times-Bold",5)
        self.c.drawRightString(70,70,"INVOICE No. :")
        tb_name=pickle.load( open( "lis.pkl", "rb" ) )
        self.c.drawRightString(85,70,tb_name)
        self.c.drawRightString(70,80,"DATE :")
        import datetime
        self.c.drawRightString(112,80,datetime.date.today().strftime("%B %d, %Y")) 
        db=pymysql.connect(host='0.tcp.ap.ngrok.io',
                                            port=pt,
                                            user='root',
                                            password='',
                                            database='')
        c=db.cursor()
        try:
            c.execute("SELECT name,phonenumber,Volume,cost FROM signup WHERE idd=%s",(tb_name))
            out=c.fetchone()
        except:
            out=['error']*4
        
        self.c.drawRightString(70,90,"CUSTOMER NAME :")
        self.c.drawRightString(70,100,"PHONE No. :")
        self.c.drawRightString(80,90,out[0])
        self.c.drawRightString(90,100,out[1])
        self.c.roundRect(15,108,170,130,10,stroke=1,fill=0)
        self.c.line(15,120,185,120)
        self.c.drawCentredString(25,118,"SR No.")
        self.c.drawCentredString(75,118,"GOODS DESCRIPTION")
        self.c.drawCentredString(125,118,"RATE")
        self.c.drawCentredString(148,118,"QTY")
        self.c.drawCentredString(173,118,"TOTAL")
        self.c.line(15,210,185,210)
        self.c.line(35,108,35,220)
        self.c.line(115,108,115,220)
        self.c.line(135,108,135,220)
        self.c.line(160,108,160,220)
        self.c.line(15,220,185,220)
        self.c.line(100,220,100,238)
        self.c.drawCentredString(75,128,"Water Usage")
        self.c.drawCentredString(125,128,"6 Rs/L")
        self.c.drawCentredString(148, 128, f"{out[2]} L" )
        self.c.drawCentredString(173,128,str(out[3]))
        
        self.c.drawString(20,225,"We declare that above mentioned")
        self.c.drawString(20,230,"information is true.")
        self.c.drawString(20,235,"(This is system generated invoive)")
        self.c.drawRightString(180,235,"Authorised Signatory")
        image = convert_from_bytes(self.c.getpdfdata(),fmt="png",output_folder=dire)[0]
        directories = os.listdir(dire)
        for file in directories:
            temp=str(file)
        self.clear_widgets()
        
        self.add_widget(Image(source=f"{dire}/{temp}",size_hint=(1,0.9),pos_hint={"top":1}))
        
        self.next=Button(text="Next",size_hint =(.25, .1),
                pos_hint ={"right":1})
        self.next.bind(on_press=self.er)
        self.add_widget(self.next)
        self.save=Button(text="Download",size_hint =(.25, .1),
                pos_hint ={'x':.25, 'y':0})
        self.save.bind(on_press=self.download)
        self.add_widget(self.save)
        self.save2=Button(text="Payment",size_hint =(.25, .1),
                pos_hint ={'x':.5, 'y':0})
        self.save2.bind(on_press=self.down)
        self.add_widget(self.save2)
    def er(self,instance):
        self.current="grap"
    def download(self,instance):

        self.c.save()
        popup = Popup(title='Downloaded', content=Label(text=f'file downloaded at:{os.getcwd()}'),size_hint=(.5,.5),auto_dismiss=True)
        popup.open()
    def down(self,instance):        
        popup = Popup(title='PAYMENT', content=Label(text='PAYMENT SUCCESSFUL'),size_hint=(.5,.5),auto_dismiss=True)
        popup.open()

        


class ScreenManager(ScreenManager):
    pass

sm = ScreenManager()
sm.add_widget(LOGIN(name='li'))
sm.add_widget(SIGN(name='SI'))

sm.add_widget(SIGN(name='bil'))
print(sm.current)
class TestApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        s=Builder.load_string(b)
        
        
        
        return ScreenManager()
    def logger(self):
        tb_name=""
        connection = pymysql.connect(host='0.tcp.ap.ngrok.io',
                             port=pt,
                             user='root',
                             password='',
                             database='')
        sq="SELECT name,password FROM signup"
        C=connection.cursor()
        C.execute(sq)
        out=C.fetchall()
        variable = {key:val for key,val in out}
        print(variable)
        print(self.root)
        addwindow_instance = self.root.get_screen('li')
        if addwindow_instance.ids["user"].text in variable.keys():
            self.user=addwindow_instance.ids['user'].text
            addwindow_instance = self.root.get_screen('li')
            

            if variable[self.user]==addwindow_instance.ids['password'].text:
                C.execute("SELECT idd FROM signup WHERE name=%s AND password=%s",(self.user,addwindow_instance.ids['password'].text))
                
                tb_name=C.fetchone()[0]
                pickle.dump( tb_name, open( "lis.pkl", "wb" ) )
                sm.add_widget(SIGN(name='grap'))
                
                
                
                self.root.current='grap'

            else:
                popup = Popup(title='ERROR', content=Label(text='INCORRECT PASSWORD !! TRY AGAIN!!'),size_hint=(.5,.5),auto_dismiss=True)
                popup.open()
            
        else:
            self.root.current='SI'
    
    def signup(self,):
        connection = pymysql.connect(host='0.tcp.ap.ngrok.io',
                             port=pt,
                             user='root',
                             password='',
                             database='fex')
        c=connection.cursor()
        addwindow_instance = self.root.get_screen('SI')
        print(addwindow_instance.ids['user'].text)
        name=addwindow_instance.ids['user'].text
        psd=addwindow_instance.ids['password'].text
        idd=addwindow_instance.ids['noc'].text
        nnoc=addwindow_instance.ids['nocs'].text
        pno=addwindow_instance.ids['pno'].text
        nop=addwindow_instance.ids['nop'].text
        print(type(idd),idd)
        sql="INSERT INTO signup (idd,name,password,phonenumber,noc,nop) VALUES (%s,%s,%s,%s,%s,%s)"
        val=(idd,name,psd,pno,nnoc,nop)
        print(val)
        c.execute(sql,val)
        connection.commit()
        
        import urllib3
        http = urllib3.PoolManager()

        resp = http.request('GET', f'{webadd}/id/{str(idd)}')
        print(resp)

        
        self.root.current='li'
        addwindow_instance = self.root.get_screen('grap')
        
        self.layout = GridLayout()
        
        pass
    def login(self):
        self.root.current="li"
    def screensi(self):
        self.root.current="SI"

if __name__ == '__main__':
    
    TestApp().run()
