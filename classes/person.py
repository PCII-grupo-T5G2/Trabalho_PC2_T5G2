import datetime
from classes.gclass import Gclass

class Person(Gclass):
    
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
            Person.refeicoes_agendadas.append([data,ementa])
            print(f"Refeição marcada para {data} com a ementa {ementa} em nome de {self._name}.")
        else:
            print("Funcionários não podem marcar refeições.")

    def consultar_reservas_por_ementa(self, data):
        if self._role == 'funcionario':
            reservas = {refeicao[1]: 0 for refeicao in Person.refeicoes_agendadas if refeicao[0] == data}
            for refeicao in Person.refeicoes_agendadas:
                if refeicao[0] == data:
                    reservas[refeicao[1]] += 1
            print("Reservas por ementa:")
            for ementa, quantidade in reservas.items():
                print(f"{ementa}: {quantidade}")





class Cliente(Person):
    def __init__(self, name, senha):
        super().__init__(name, 'cliente', senha)

class Funcionario(Person):
    def __init__(self, name, senha):
        super().__init__(name, 'funcionario', senha)
        
cliente = Cliente("João", "12345")
cliente.marcar_refeicao("2024-03-27", "Feijoada")

cliente1 = Cliente('Miguel', '123')
cliente1.marcar_refeicao("2024-03-27", "Feijoada")

cliente2 = Cliente('Afonso', '1234')
cliente2.marcar_refeicao("2024-03-27", "Feijoada")

cliente3 = Cliente('Edu', '1236')
cliente3.marcar_refeicao('2024-03-27', 'Carne')


funcionario = Funcionario("Maria", "54321")
funcionario.consultar_reservas_por_ementa("2024-03-27")
