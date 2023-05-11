class Reserva:
    def __init__(self, data_entrada, data_saida):
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.quartos_reservados = []  # Lista de quartos reservados para essa reserva

    # Métodos de acesso aos quartos reservados
    def adicionar_quarto_reservado(self, quarto):
        self.quartos_reservados.append(quarto)

    def remover_quarto_reservado(self, quarto):
        self.quartos_reservados.remove(quarto)
