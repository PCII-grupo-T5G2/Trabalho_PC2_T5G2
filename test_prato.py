# -*- coding: utf-8 -*-
"""
Created on Wed May 22 14:54:21 2024

@author: joaop
"""

from datafile import filename

from classes.prato import Prato

Prato.read(filename + 'cantina.db')

cname = "Prato"
cl = eval(cname)

obj = cl.from_string("1004;2;bife;pescada;tofu")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("1003;3;francesinha;bacalhau;lentilhas")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos objetos gravados " ,cl.lst)
