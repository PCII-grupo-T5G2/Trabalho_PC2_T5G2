

from classes.prato import Prato

Prato.read('data/cantina.db')

cname = "Prato"
cl = eval(cname)

obj = cl.from_string("2024-05-29;almoco")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos objetos gravados " ,cl.lst)