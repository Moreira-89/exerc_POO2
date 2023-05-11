from datetime import date
from quarto import Quarto
from hospede import Hospede
from reserva import Reserva

# Código para testar o sistema de reservas de hotéis

# Exemplo de criação de objetos Quarto
quarto1 = Quarto(2, 1, 0, 0, 1, True, False, True, True, 200)
quarto2 = Quarto(4, 2, 1, 1, 0, False, True, True, True, 300)

# Exemplo de criação de objetos Hospede
hospede1 = Hospede("Fulano de Tal", date(1990, 5, 10), "123456789")
hospede2 = Hospede("Ciclano da Silva", date(1985, 9, 20), "987654321")

# Exemplo de criação de objetos Reserva
reserva1 = Reserva(date(2023, 5, 15), date(2023, 5, 20))
reserva1.quartos_reservados.append(quarto1)
reserva1.quartos_reservados.append(quarto2)
quarto1.hospedes_reservados = [hospede1]
quarto2.hospedes_reservados = [hospede2]

