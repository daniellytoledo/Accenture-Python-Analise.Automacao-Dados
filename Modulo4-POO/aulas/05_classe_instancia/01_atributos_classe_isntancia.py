class Estudante:
    escola = "DIO" # atributo
    # escola = Variável de classe.
    # Pertence à classe Estudante e é compartilhada por todos os objetos.
    # Se nenhum objeto criar sua própria variável 'escola',
    # todos acessarão este mesmo valor.

    def __init__(self, nome, matricula): # construtor, executado automaticamente toda vez que um novo objeto é criado.

        self.nome      = nome # variável (atributo) de instância
        self.matricula = matricula # cada objeto possui a sua própria matrícula
    
    def __str__(self) -> str: # método string
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# criando uma instância (objeto) de classe Estudante
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)

# alterando apenas a matrícula do objeto aluno_1
# como matrícula é uma variável de instância, essa alteração não afeta aluno_2
aluno_1.matricula = 3
mostrar_valores(aluno_1, aluno_2)