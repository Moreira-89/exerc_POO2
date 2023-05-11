class Quarto:
    def __init__(self, capacidade, camas_solteiro, camas_casal, camas_queen, camas_king, frigobar, sacada, banheiro_privativo, tv, preco_diaria):
        self.capacidade = capacidade
        self.camas_solteiro = camas_solteiro
        self.camas_casal = camas_casal
        self.camas_queen = camas_queen
        self.camas_king = camas_king
        self.frigobar = frigobar
        self.sacada = sacada
        self.banheiro_privativo = banheiro_privativo
        self.tv = tv
        self.preco_diaria = preco_diaria
        self.hospedes_reservados = []  # Lista de hóspedes reservados para esse quarto

    # Métodos de acesso aos hóspedes reservados
    def adicionar_hospede_reservado(self, hospede):
        self.hospedes_reservados.append(hospede)

    def remover_hospede_reservado(self, hospede):
        self.hospedes_reservados.remove(hospede)
