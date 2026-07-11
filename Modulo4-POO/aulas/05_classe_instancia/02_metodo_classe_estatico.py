# Método de Classe

# Métodos de classe estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto.

# Métodos estáticos

# Um método estático não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe.

# Métodos de classe x Métodos estáticos:

# Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
# Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo.

# Quando utilizar método de classe ou estático:

# Geralmente usamos o método de classe para criar métodos de fábrica
# Geralmente usamos métodos estáticos para criar funções utilitárias

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade


     # método de class, recebe a própria classe (cls) como primeiro parâmetro em vez da instâcia (self)
     # retorna Pessoa(nome, idade), mas usar cls permite que o método funcione também em classes que herdam de Pessoa.
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade)
    
    # não recebe nem self (instância), nem cls (classe)
    # é usado quando o método apenas executa uma tarefa relacionada à classe, mas não precisa acessar atributos da instância nem da classe
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# criando um objeto utilizando o construtor tradicional Pessoa()
""" p = Pessoa("Guilherme", 47)
print(p.nome, p.idade) """

# método classe
# ao invés de informarmos idade, informamos a data de nascimento e ele calcula quantos anos o usuário tem
p2 = Pessoa.criar_de_data_nascimento(1991, 11, 26, "Danielly")
print(p2.nome, p2.idade)

# chamando o método estático
# como ele não depende de um objeto específico, pode ser chamado diretamente pela classe
print(Pessoa.e_maior_idade(17)) # False
print(Pessoa.e_maior_idade(19)) # True

# self = eu (o objeto)
# cls = nós (a classe)
# staticmethod = independente (não precisa de nenhum dos dois)