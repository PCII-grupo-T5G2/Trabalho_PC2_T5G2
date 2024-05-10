import datetime
import sqlite3

from classes.gclass import Gclass

class Utilizador(Gclass):
    
    refeicoes_agendadas = []
    
    def __init__(self, name, role, senha):
        super().__init__()
        self._name = name
        self._role = role  # 'cliente' ou 'funcionario'
        self._senha = senha

    @property
    def name(self):
        return self._name

    @property
    def role(self):
        return self._role

    @property
    def senha(self):
        return self._senha
    

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
    
    



        
cliente = Utilizador("João", 'cliente', "12345")
cliente.marcar_refeicao("2024-03-27", "Feijoada")

cliente1 = Utilizador('Miguel', 'cliente', '123')
cliente1.marcar_refeicao("2024-03-27", "Feijoada")

cliente2 = Utilizador('Afonso', 'cliente', '1234')
cliente2.marcar_refeicao("2024-03-27", "Feijoada")

cliente3 = Utilizador('Edu', 'cliente', '1236')
cliente3.marcar_refeicao('2024-03-27', 'Carne')

cliente3 = Utilizador('Diogo', 'cliente', '1239')
cliente3.marcar_refeicao('2024-03-28', 'Vegetariano')




funcionario = Utilizador("Maria", 'funcionario', "54321")
funcionario.consultar_reservas_por_ementa("2024-03-27")
