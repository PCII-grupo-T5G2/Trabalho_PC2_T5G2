from Classes.ementa import Ementa


class Reserva(self, data, ementa, codigoReserva):
    self._data=data
    self._ementa=ementa
    self._codigoReserva=codigoReserva


    @property
    def data(self):
        return self._data
    

    @property
    def ementa(self):
        return self._ementa
    

    @property
    def codigoReserva(self):
        return self._codigoReserva
    
    