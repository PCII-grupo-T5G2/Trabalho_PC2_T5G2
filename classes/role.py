from classes.gclass import Gclass

class Role(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_funcao', '_nome']
    # Class header title
    header = 'Role'
    # field description for use in, for example, in input form
    des = ['Funcao', 'Nome']
    # Constructor: Called when an object is instantiated
    
    def __init__(self, funcao, nome):
        super().__init__()
        self._funcao=funcao
        self._nome=nome

    @property
    def funcao(self):
        return self._funcao
    
    @property
    def nome(self):
        return self._nome