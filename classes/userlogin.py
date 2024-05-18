"""
@author: António Brito / Carlos Bragança
(2024) #objective: class Person
"""""
# Class User - generic version
# import sys
import bcrypt

from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_user','_usergroup','_password']
    
    header = 'Users'
    
    des = ['User','User group','Password']
    username = ''
    
    def __init__(self, user, usergroup, password):
        super().__init__()
        
        self._user = user
        self._usergroup = usergroup
        self._password = password
        
        Userlogin.obj[user] = self
        
        Userlogin.lst.append(user)

    
    @property
    def user(self):
        return self._user
    
    @property
    def usergroup(self):
        return self._usergroup
    
    @usergroup.setter
    def usergroup(self, usergroup):
        self._usergroup = usergroup
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = self.set_password(password)

    @classmethod
    def chk_password(self, user, password):
        Userlogin.username = ''
        if user in Userlogin.obj:
            obj = Userlogin.obj[user]
            if obj._password == password:
                valid = True
            else: 
                valid = False
            #valid = bcrypt.checkpw(password.encode(), obj._password.encode())
            if valid:
                Userlogin.username = user
                message = "Valid"
            else:
                message = 'Wrong password'
        else:
            message = 'No existent user'
        return message
    


    @classmethod
    def set_password(self, password):
        passencrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return passencrypted.decode()
