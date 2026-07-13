# Desafio
# Você trabalha em uma consultoria de TI que está desenvolvendo um sistema para padronizar o cadastro de diferentes tipos de colaboradores. Seu papel é ensinar um novo programador sobre a importância de abstração e interfaces para garantir que todos os tipos de colaboradores sigam um mesmo padrão de comportamento, facilitando futuras expansões do sistema. Para isso, você deve criar uma estrutura abstrata que defina um método obrigatório para exibir informações do colaborador, e implementar uma classe concreta que represente um Analista, seguindo esse padrão. O objetivo é garantir que, ao receber o nome de um Analista, o sistema consiga exibir corretamente suas informações, demonstrando o uso de classes abstratas e interfaces.

# Implemente uma classe abstrata chamada Colaborador com um método abstrato exibir_info(). Em seguida, crie uma classe Analista que herda de Colaborador e implementa o método exibir_info(), retornando a string "Analista: " seguida do nome recebido. O programa deve ler o nome do Analista e exibir a saída conforme o padrão definido. Não utilize bibliotecas externas, apenas recursos padrão da linguagem.

# Entrada
# Uma única linha contendo o nome do Analista (string, pode conter letras e espaços).

# Saída
# Uma única linha com a string "Analista: " seguida do nome informado na entrada.

from abc import ABC, abstractmethod

# Classe abstrata para padronizar colaboradores
class Colaborador(ABC):
    @abstractmethod
    def exibir_info(self):
        pass

# Classe concreta para Analista
class Analista(Colaborador):
    def __init__(self, nome):
        self.nome = nome

    def exibir_info(self):
        # TODO: Retorne a string no formato "Analista: " seguido do nome do analista
        return f"Analista: {self.nome}"

nome_analista = input()
analista = Analista(nome_analista)
print(analista.exibir_info())