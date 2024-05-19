from classes.ementa import Ementa

class Prato(Ementa):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_nome','_descricao', '_preco']
    # Class header title
    header = 'Prato'
    # field description for use in, for example, in input form
    des = ['Nome','Descricao', 'Preco']
    # Constructor: Called when an object is instantiated
    

    def __init__(self, nome: str, descricao: str, preco: int):
        super().__init__()
        self._nome=nome
        self._descricao=descricao
        self._preco=preco
        
        Prato.obj[nome] = self

        Prato.lst.append(nome)
    

    @property
    def nome(self):
        return self._nome
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def preco(self):
        return self._preco
    

    