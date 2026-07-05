class Animal():
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self): 
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, nro_patas, cor_pelo):
        self.cor_pelo = cor_pelo
        super().__init__(nro_patas)

class Ave(Animal):
    def __init__(self, nro_patas):
        super().__init__(nro_patas)

class Gato(Mamifero):
    pass

class Onitorrinco(Mamifero):
    pass

gato = Gato(4, "preto")
print(gato)