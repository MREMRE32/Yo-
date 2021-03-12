import kivy
#kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
#from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from account import Account
import pickle

# kivy_venv\Scripts\activate
savefile = "accounts.pickle"

class Menu(BoxLayout, Screen): #HI THERE
    def btn(self):
        show_popup()
    def btn2(self):
        sign_popup()

class Sign(FloatLayout):
        
    def createAccount(self):
        email = self.ids.email
        uname = self.ids.uname
        pass1 = self.ids.pass1
        pass2 = self.ids.pass2
        pass1.hint_text = "yo"
    	

        if(email.text != "" and uname.text != "" and pass1.text != "" and pass2.text != "" and pass2.text == pass1.text):
            newacc = Account(email.text,uname.text,pass1.text)
            if (newacc.valid == True): # Class init checks if the email is valid.
                create_popup()
                newacc.localSave(savefile)
            else:
                not_success()
        else:
            not_success()
        # Need to validate information before creating the popup

class Log(FloatLayout):
    def verifyAccount(self):
        LogUser = self.ids.LogUser
        LogPass = self.ids.LogPass
        logacc = Account.getSave(savefile)
        print("Username: "+LogUser.text)
        print("Password: "+LogPass.text)
        if (logacc.username == LogUser.text and logacc.password == LogPass.text):
            log_success()

class P3(FloatLayout):
    pass

class P4(FloatLayout):
    pass

class P5(FloatLayout):
    pass

class Terms(BoxLayout, Screen):
    pass

def show_popup():
    show = Log()
    popupWindow = Popup(title="", content = show, size_hint = (None,None), size=(250,250))
    popupWindow.open()
def sign_popup():
    sign = Sign()
    popupWindow = Popup(title="", content=sign, size_hint=(None, None), size=(250, 400))
    popupWindow.open()
def create_popup():
    create = P3()
    popupWindow = Popup(title="", content=create, size_hint=(None, None), size=(220, 200))
    popupWindow.open()
def not_success():
    nots = P4()
    popupWindow = Popup(title="", content=nots, size_hint=(None, None), size=(450, 200))
    popupWindow.open()
def log_success():
    login = P5()
    popupWindow = Popup(title="", content=login, size_hint=(None, None), size=(450, 200))
    popupWindow.open()

class Manager(ScreenManager):
    pass

class Opening(App):
    def build(self):
        return Manager()

if __name__ == "__main__":
    sa = Opening()
    sa.run()