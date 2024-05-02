class Prato():
    obj=dict()
    lst=list()
    ind=0
    

    def __init__(self, nome: str, descricao: str, preco: int):
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
    

    