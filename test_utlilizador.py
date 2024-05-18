# -*- coding: utf-8 -*-
"""
Created on Sat May 18 16:39:28 2024

@author: joaop
"""

from datafile import filename

from classes.Utilizador import Utilizador

Utilizador.read(filename + 'cantina.db')

cname = "Utilizador"
cl = eval(cname)

obj = cl.from_string("1004;Edu;aluno;edu;edu@gmail.com")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("1003;Saraiva;funcionário;saraiva;saraiva@gmail.com")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos objetos gravados " ,cl.lst)

