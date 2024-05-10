from classes.gclass import Gclass

class Role(Gclass):
    def __init__(self, funcao, nome):
        self._funcao=funcao
        self._nome=nome

    @property
    def funcao(self):
        return self._funcao
    
    @property
    def nome(self):
        return self._nome