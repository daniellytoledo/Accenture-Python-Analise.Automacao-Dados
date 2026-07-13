# Interfaces definem o que uma classe deve fazer e não como

# O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas para criar contratos. Classes abstradas não podem ser instanciadas.

# ABC

# Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é ABC. O ABC funciona decorando métodos da classe base como abstrados e, em seguida, registrando classes concretas como implementações da base abstrata. Um método se torna abstrato quando decorado com @abstractmethod

# O que é uma classe abstrata?

# Uma classe abstrata serve como um modelo para outras classes.
# Ela define quais métodos as classes filhas devem obrigatoriamente possuir, mas não diz como eles serão implementados.

# ABC → transforma a classe em uma classe abstrata.
# @abstractmethod → torna um método obrigatório para as classes filhas.
# Classe abstrata → serve como um modelo e não pode ser instanciada.
# Classe concreta → implementa todos os métodos abstratos e pode ser instanciada.

from abc import ABC, abstractmethod

# hernando de abc, essa classe não pode ser instanciada diretamente
class ControleRemoto(ABC):
    # método abstrato, toda classe que herdar de controle remoto será obrigada a implementar este método
    @abstractmethod
    def ligar(self):
        pass

    # método abstrato
    @abstractmethod
    def desligar(self):
        pass

# classe concreta que herda da classe abstrata ControleRemoto
# como ela implementou todos os métodos abstratos, agora pode ser instanciada normalmente
class ControleTV(ControleRemoto):
    # implementação do método ligar()
    def ligar(self):
        print("Ligando a TV...")

    # implementação do método desligar()
    def desligar(self):
        print("Desligando a TV...")

# cria um objeto de classe ControleTV
controle = ControleTV()

controle.ligar()
controle.desligar()