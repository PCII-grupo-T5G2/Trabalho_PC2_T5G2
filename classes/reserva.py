from classes.gclass import Gclass

class Reserva(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_data','_prato', '_codigoReserva']
    # Class header title
    header = 'Reserva'
    # field description for use in, for example, in input form
    des = ['Data', 'Prato', 'CodigoReserva']
    # Constructor: Called when an object is instantiated

    def __init__(self, data, prato, codigoReserva):
        super().__init__()
        self._data=data
        self._prato=prato
        self._codigoReserva=codigoReserva


    @property
    def data(self):
        return self._data
    

    @property
    def prato(self):
        return self._ementa
    

    @property
    def codigoReserva(self):
        return self._codigoReserva
    
    