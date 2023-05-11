from datetime import date
from quarto import Quarto
from hospede import Hospede
from reserva import Reserva

# Exemplo de criação de objetos Quarto
quarto1 = Quarto(2, 1, 0, 0, 1, True, False, True, True, 200)
quarto2 = Quarto(4, 2, 1, 1, 0, False, True, True, True, 300)

# Exemplo de criação de objetos Hospede
hospede1 = Hospede("Lucas Moreira", date(2003, 6, 3), "123456789")
hospede2 = Hospede("Leandro Luque", date(1985, 9, 20), "987654321")

# Exemplo de criação de objetos Reserva
reserva1 = Reserva(date(2023, 5, 15), date(2023, 5, 20))

# Realizar uma reserva
reserva1.quartos_reservados.append(quarto1)
quarto1.hospedes_reservados.append(hospede1)

# Exibir detalhes da reserva
print("Detalhes da Reserva:")
print("Data de Entrada:", reserva1.data_entrada)
print("Data de Saída:", reserva1.data_saida)
for quarto in reserva1.quartos_reservados:
    print("--- Quarto ---")
    print("Capacidade:", quarto.capacidade)
    print("Preço Diária:", quarto.preco_diaria)
    print("Hóspedes:")
    for hospede in quarto.hospedes_reservados:
        print("- Nome:", hospede.nome)
        print("- Data de Nascimento:", hospede.data_nascimento)
        print("- CPF:", hospede.cpf)
    print("---------------")
