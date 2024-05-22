from datetime import date, datetime

from classes.gclass import Gclass

class Reserva(Gclass):
    
    num = 1000
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_codigoReserva', '_data','_prato']
    # Class header title
    header = 'Reserva'
    # field description for use in, for example, in input form
    des = ['CodigoReserva','Data', 'Prato']
    # Constructor: Called when an object is instantiated

    def __init__(self, codigoReserva, data, prato):
        super().__init__()
        self._data = datetime.strptime(data, '%Y-%m-%d').date()
        self._prato= prato
        self._codigoReserva = Reserva.num
        Reserva.num += 1
        Reserva.obj[self._codigoReserva] = self
        Reserva.lst.append(self._codigoReserva)
        
    @property
    def data(self):
        return self._data
    
    @property
    def prato(self):
        return self._prato

    @property
    def codigoReserva(self):
        return self._codigoReserva
    
    def __str__(self):
        return f'{self._data};{self._prato};{self._codigoReserva}'

