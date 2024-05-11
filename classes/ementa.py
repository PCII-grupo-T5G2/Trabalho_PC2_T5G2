from classes.gclass import Gclass

class Ementa(Gclass):
    def __init__(self, nome, pratocarne, pratopeixe, pratoveg):
        super().__init__()
        self._nome = nome
        self._pratocarne = pratocarne
        self._pratopeixe = pratopeixe
        self._pratoveg = pratoveg

    @property
    def nome(self):
        return self._nome
    
    @property
    def pratocarne(self):
        return self._pratocarne
    
    @property
    def pratopeixe(self):
        return self._pratopeixe
    
    @property
    def pratoveg(self):
        return self._pratoveg
    

    
    