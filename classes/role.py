from classes.gclass import Gclass

class Role(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_nome', '_funcao']
    # Class header title
    header = 'Role'
    # field description for use in, for example, in input form
    des = ['Nome', 'Funcao']
    # Constructor: Called when an object is instantiated
    
    def __init__(self, nome, funcao):
        super().__init__()
        self._funcao=funcao
        self._nome=nome
        
        Role.obj[nome] = self

        Role.lst.append(nome)

    @property
    def funcao(self):
        return self._funcao
    
    @property
    def nome(self):
        return self._nome