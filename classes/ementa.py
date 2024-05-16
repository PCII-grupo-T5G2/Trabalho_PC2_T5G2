from classes.gclass import Gclass

class Ementa(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_nome','_pratocarne', '_pratopeixe', '_pratoveg']
    # Class header title
    header = 'Ementa'
    # field description for use in, for example, in input form
    des = ['Nome','Pratocarne', 'Pratopeixe', 'Pratoveg']
    # Constructor: Called when an object is instantiated
    
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
    

    
    