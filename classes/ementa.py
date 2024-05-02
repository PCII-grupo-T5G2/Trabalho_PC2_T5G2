class Ementa():
    def __init__(self, nome, pratos):
        self._nome=nome
        self._pratos=pratos


    @property
    def nome(self):
        return self._nome
    
    @property
    def pratos(self):
        return self._pratos
    
    