class Bicicleta:
    def __init__ (self, cor, modelo, ano, valor):
        self.cor    = cor    # atributo
        self.modelo = modelo # atributo
        self.ano    = ano    # atributo
        self.valor  = valor  # atributo

    # neste def estamos criando uma definição de construtor usando __init__
    # o self é uma referência ao objeto, é um atributo que reprefesenta a instância do objeto. poderia ser outro nome como this, mas o self é uma boa prática, além de que o this pegaria apenas o escopo "local", não pegaria referência externa. essa função dentro da classe está servindo para definir as caracteristicas da classe que neste caso é a bicicleta

    # o self serve como argumento, sem um argumento, a função gera um erro

    def buzinar(self): # criando métodos
        print("PLIM PLIM!!!!")

    def parar(self): 
        print("parando bicicleta...")
        print("Bicicleta parada.")

    def correr(self):
        print("VRUM!!!!!!!!!!!!!!")

    # métodos são funções que estão dentro de uma classe
    # também podemos definir funções para printar as caracteristicas da bicicleta

    # __str__ para poder usar a string como f"" e mostrar as caracteristicas do self. esse código não é de boa prática porque neste caso, precisamos escrever toda a chave e valor manualmente:
    def __str__(self): 
        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}."
    
    # função pra mostrar o nome da classe e as caracteristicas em dicionário automaticamente:
    def __str__(self): 
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
        # ', '.join coloca toda a lista pra concatenar com uma string especifica que neste caso é a vírgula e um espaço. ao invés de mostrar as caracteristicas como uma lista entre '', ele vai separar cada uma delas com uma vírgula.
        # self.__dict__ em si retorna um dicionário, então pra mostrar como lista podemos usar o .items() 
        # como estamos usando uma função para mostrar em str o nome da classe, neste caso, referindo como self, mesmo que o nome dela mude posteriormente, não precisaremos nos preocupar em mudar todo o código
        # o mesmo serve para chave=valor, o "for chave, valor in" faz com que o código percorra tudo que está declarado dentro de def __init__, mostrando a chave e seu valor, então caso alguém acrescente mais alguma caracteristica dentro, o código vai continuar mostrando tudo

bicicleta_1 = Bicicleta("vermelha", "caloi", 2022, 600)

print("\n")
bicicleta_1.buzinar()

print("\n")
bicicleta_1.parar()

print("\n")
bicicleta_1.correr()

print("\n")

print("A cor da bicicleta_1 é: ", bicicleta_1.cor,".", "O modelo da bicicleta_1 é: ", bicicleta_1.modelo,".", "O ano da bicicleta_1 é: ", bicicleta_1.ano,".", "A bicicleta_1 custa: ", bicicleta_1.valor, "reais.")

