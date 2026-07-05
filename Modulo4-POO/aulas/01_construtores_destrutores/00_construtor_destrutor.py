# Método construtor:
# O método construtor sempre é executado quando uma nova instância da classe é criada. Nesse método inicializamos o estado do nosso objeto. Para declarar o método construtor da classe, criamos um método com o nome __init__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome     = nome     # atributo
        self.cor      = cor      # atributo
        self.acordado = acordado # atributo

    def __del__(self):
        print("Removendo a instância da classe...")

    def falar(self):
        print("auau!")
              
c = Cachorro("Chappie", "amarelo")
c.falar()

# Método destrutor:
# O método destrutor sempre é executado quando uma instância (objeto) é destruída. Destrutores em Python não são tão necessários como em C++ porque Python tem um coletor de lixo que lida com o gerenciamerento de memória automaticamente. Para declarar o método destrutor da classe, criamos um método com o nome __del__
# em outras palavras, é um método especial do Python que é chamado quando um objeto está prestes a ser destruído na memória. Sua principal finalidade é liberar recursos, como fechar arquivos, conexões de banco de dados ou sockets.
# uma boa prática é não confiar no __del__, pois pode ser que ele não seja chamado imediatamente. O Python possui um coletor de lixo Garbage Collector e ele decide quando destruir os objetos. Por isso o recomendado é usar context managers (with).

# with open("arquivo.txt") as arquivo:
#   print(arquivo.read())

# quando o bloco termina
# arquivo.close()

