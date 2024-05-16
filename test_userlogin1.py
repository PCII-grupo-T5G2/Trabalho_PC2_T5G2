from datafile import filename

from classes.userlogin import Userlogin

Userlogin.read(filename + 'cantina.db')

cname = "Userlogin"
cl = eval(cname)

obj = cl.from_string("Edu;aluno;edu")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("Saraiva;funcionário;saraiva")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos objetos gravados " ,cl.lst)

