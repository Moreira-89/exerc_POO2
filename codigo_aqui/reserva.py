from datetime import date

class Reserva:
    def __init__(self, data_entrada, data_saida):
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.quartos_reservados = []
