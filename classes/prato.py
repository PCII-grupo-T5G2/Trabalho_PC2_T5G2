from classes.gclass import Gclass

class Prato(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_cod','_semana','_nome', '_tipo']
    # Class header title
    header = 'Prato'
    # field description for use in, for example, in input form
    des = ['Cod','Semana', 'Nome','Tipo']
    # Constructor: Called when an object is instantiated
    

    def __init__(self, cod,semana,nome,tipo):
        super().__init__()
        self._cod = cod
        self._semana = semana
        self._nome = nome
        self._tipo = tipo
        
        Prato.obj[cod] = self

        Prato.lst.append(cod)
    

    @property
    def cod(self):
        return self._cod
    
    @property
    def semana(self):
        return self._semana
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def tipo(self):
        return self._tipo
    
    def procuraNovoCodigo():
        maior_codigo = 0
        if len(Prato.lst) > 0:
            return int(Prato.lst[-1])
        return maior_codigo
    

    
