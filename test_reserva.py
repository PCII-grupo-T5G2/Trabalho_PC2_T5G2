
from classes.reserva import Reserva

Reserva.read('data/cantina.db')

cname = "Reserva"
cl = eval(cname)
    
obj = cl.from_string("1001;2024-05-29;almoco")

print("objeto sem estar gravado ",obj)

cl.insert(getattr(obj,cl.att[0]))


print("\nLista dos objetos gravados " ,cl.lst)