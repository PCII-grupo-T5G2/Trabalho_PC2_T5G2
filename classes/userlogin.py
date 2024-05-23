"""
@author: António Brito / Carlos Bragança
(2024) #objective: class Person
"""""
# Class User - generic version
# import sys
import bcrypt
from flask import session
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    att = ['_email','_usergroup','_password']
    
    header = 'Email'
    
    des = ['Email','User group','Password']
    username = ''
    
    def __init__(self, email, usergroup, password):
        super().__init__()
        
        self._email = email
        self._usergroup = usergroup
        self._password = password
        
        Userlogin.obj[email] = self
        
        Userlogin.lst.append(email)

    
    @property
    def email(self):
        return self._email
    
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
                session["user"] = user
                session["usergroup"] = obj._usergroup
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
