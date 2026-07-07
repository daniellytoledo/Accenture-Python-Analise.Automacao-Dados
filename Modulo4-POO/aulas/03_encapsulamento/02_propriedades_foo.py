# Propriedades. Pra que serve?

# Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe.

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # transforma o método x() em uma propriedade, assim podemos acessar foo.x como um atributo, sem precisar escrever foo.x()
    def x(self):
        return self._x
    
    @x.setter # executado quando fazemos foo.x = valor. neste exemplo, ele soma o novo valor ao valor atual
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0 # é uma forma de reiniciar o valor, igualando à zero. não necessariamente deletando porque o _x continua existindo

foo = Foo(10)
print(foo.x) # 10

print("-"*15)

foo.x = 10
print(foo.x) # 20 (pegou o valor 10 anterior e somou mais 10 pela função dentro definida no setter)

print("-"*15)

del foo.x # quando usamos o del foo.x, o método @x.deleter é executado. neste exemplo, ele não remove o atributo, apenas altera seu valor para 0
print(foo.x) # 0

print("-"*15)

foo.x       # chama automaticamente o getter (property)
foo.x = 10  # chama automaticamente o setter
del foo.x   # chama automaticamente o deleter