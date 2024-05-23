import datetime

from classes.gclass import Gclass
from classes.reserva import Reserva

class Utilizador(Gclass):
    refeicoes_agendadas = []
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    
    # class attributes, identifier attribute must be the first one on the list
    att = ['_codigo','_name','_role', '_senha', '_email']
    # Class header title
    header = 'Utilizador'
    # field description for use in, for example, in input form
    des = ['Codigo','Name','Role', 'Senha', 'Email']
    # Constructor: Called when an object is instantiated
    
    def __init__(self, codigo, name, role, senha, email):
        super().__init__()
        self._codigo = codigo
        self._name = name
        self._role = role #cliente ou funcionario
        self._senha = senha
        self._email = email
        Utilizador.obj[codigo] = self

        Utilizador.lst.append(codigo)
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def name(self):
        return self._name

    @property
    def role(self):
        return self._role

    @property
    def senha(self):
        return self._senha

    @property
    def email(self):
        return self._email
    
    def procuraNovoCodigo():
        maior_codigo = 0
        if len(Utilizador.lst) > 0:
            return int(Utilizador.lst[-1])
        return maior_codigo
    
    def marcar_refeicao(self, data, prato):
        if self._role == "cliente":
            reserva = Reserva(data, prato)
            Utilizador.refeicoes_agendadas.append(reserva)
        else:
            print("Funcionários não podem marcar refeições.")
        
    def consultar_refeicao(self):
        for refeicao in Utilizador.refeicoes_agendadas:
            print(refeicao)
            
        

    
    
