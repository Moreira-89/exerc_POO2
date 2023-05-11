__Nome__: Lucas M. A. Rodrigues

__Prof. Dr.__ Leandro Luque

## Prática 04: Orientado a Objeto

### O que temos que fazer? 
* Reserva de Hotéis: 
  * Crie um sistema de reservas de hotéis, onde os usuários podem pesquisar e reservar quartos. Cada quarto tem um número máximo de hóspedes, a quantidade de camas de solteiro, casal, queen e king que tem, se tem frigobar, se tem sacada, sem tem banheiro privativo, se tem tv e o preço base de diária do quarto. 
  * Uma reserva tem uma data de entrada/saída (use o tipo: LocalDate), pode ter vários quartos e, para cada quarto, tem os hóspedes que nele se hospedam. Para cada hóspede, é necessário sabe o nome completo, data de nascimento e CPF. Crie um programa principal para testar o seu sistema.
***
### Minha Resolução:
Seguindo com o que o professor pediu a seguir está a minha resolução, só que antes eu queria falar algo: 
* Assim como no exercício anterior [exerc_POO](https://github.com/Moreira-89/exer_POO) desenvolvi o sistema utilizando a linguagem Python;
* Criei as classes em arquivos separados para ficar mais organizado.

__Programa Principal (exerc_POO2/codigo_aqui/prog_principal.py)__
```
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
```
__Classe Quarto (exerc_POO2/codigo_aqui/quarto.py)__
```
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
```
__Classe Reserva (exerc_POO2/codigo_aqui/reserva.py)__
```
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
```
__Classe Hospede (exerc_POO2/codigo_aqui/hospede.py)__
```
class Hospede:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
```
***
