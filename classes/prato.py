from classes.gclass import Gclass

class Prato(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_cod','_semana', '_carne','_peixe',"_vegetariano"]
    # Class header title
    header = 'Prato'
    # field description for use in, for example, in input form
    des = ['Cod','Semana', 'Carne','Peixe','Vegetariano']
    # Constructor: Called when an object is instantiated
    

    def __init__(self, cod,semana,carne,peixe,vegetariano):
        super().__init__()
        self._cod = cod
        self._semana = semana
        self._carne = carne
        self._peixe = peixe
        self._vegetariano = vegetariano
        
        Prato.obj[cod] = self

        Prato.lst.append(cod)
    

    @property
    def cod(self):
        return self._cod
    
    @property
    def semana(self):
        return self._semana
    
    @property
    def carne(self):
        return self._carne
    
    @property
    def peixe(self):
        return self._peixe
    
    @property
    def vegetariano(self):
        return self._vegetariano
    

    