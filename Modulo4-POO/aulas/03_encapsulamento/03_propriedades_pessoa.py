class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome           = nome
        self._ano_nascimento = ano_nascimento

    @property # ler o nome
    def nome(self):
        return self._nome
    
    @property # função pra ler a idade
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Danielly", 1991)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")