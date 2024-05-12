from datafile import filename

from classes.userlogin import Userlogin


Userlogin.read(filename + 'cantina.db')

cname = "Userlogin"
cl = eval(cname)

obj = cl.from_string("miguelleal13;aluno;miguel")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))

obj = cl.from_string("João;funcionário;João")
cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos onjetos gravados " ,cl.lst)


