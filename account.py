# Account class file
import re
import pickle

class Account():
    def __init__(self,email, username, password):
        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email)):
            self.valid = True
            self.email = email
            self.username = username
            self.password = password
        else:
            # RegEx email check didnt work.
            self.valid = False
    def transConvert(self):
        # Converts account class to dictionary for transport.
        out = {}
        out["email"] = self.email
        out["username"]  = self.username
        out["password"] = self.password
        return out
    def localSave(self,file):
        # Saves account locally to a pkl file
        if (self.valid == True):
            pickle_out = open(file,"wb")
            pickle.dump(self, pickle_out)
            pickle_out.close()
            return True
        else:
            return False
    def getSave(file):
        pickle_out = open(file,"rb")
        out = pickle.load(pickle_out)
        pickle_out.close()
        return out

            
