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
import pickle

Accounts = [] #list of accounts with information

pickle_in = open("accounts.pickle", "rb")
Accounts = pickle.load(pickle_in)

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
            Accounts.append([email.text, uname.text, pass1.text])
            create_popup()
        else:
            not_success()
        # Need to validate information before creating the popup

class Log(FloatLayout):
    def verifyAccount(self):
        LogUser = self.ids.LogUser
        LogPass = self.ids.LogPass
        for row in Accounts:
            if row[1] == LogUser.text and row[2] == LogPass.text:
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

#Accounts.clear() #for testing purposes
print(Accounts)
pickle_out = open("accounts.pickle","wb")
pickle.dump(Accounts, pickle_out)
pickle_out.close()