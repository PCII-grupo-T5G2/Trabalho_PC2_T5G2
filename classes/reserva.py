from classes.gclass import Gclass

class Reserva(Gclass):

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
    
    