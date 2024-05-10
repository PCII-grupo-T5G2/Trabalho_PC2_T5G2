import datetime

from classes.gclass import Gclass

class Utilizador(Gclass):
    
    refeicoes_agendadas = []
    
    def __init__(self, name, role, senha, email):
        super().__init__()
        self._name = name
        self._role = role #cliente ou funcionario
        self._senha = senha
        self._email = email
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
    

    def marcar_refeicao(self, data, ementa):
        if self._role == 'cliente':
            Utilizador.refeicoes_agendadas.append([data,ementa])
            print(f"Refeição marcada para {data} com a ementa {ementa} em nome de {self._name}.")
        else:
            print("Funcionários não podem marcar refeições.")

    def consultar_reservas_por_ementa(self, data):
        if self._role == 'funcionario':
            reservas = {refeicao[1]: 0 for refeicao in Utilizador.refeicoes_agendadas if refeicao[0] == data}
            for refeicao in Utilizador.refeicoes_agendadas:
                if refeicao[0] == data:
                    reservas[refeicao[1]] += 1
            print("Reservas por ementa:")
            for ementa, quantidade in reservas.items():
                print(f"{ementa}: {quantidade}")
    
    
