from classes.ementa import Ementa

class Prato(Ementa):
    obj=dict()
    lst=list()
    ind=0
    

    def __init__(self, nome: str, descricao: str, preco: int):
        super().__init__()
        self._nome=nome
        self._descricao=descricao
        self._preco=preco
    

    @property
    def nome(self):
        return self._nome
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def preco(self):
        return self._preco
    

    