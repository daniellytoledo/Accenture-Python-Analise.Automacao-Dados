# Desafio
# Você foi contratado por uma startup de tecnologia que está desenvolvendo um sistema de cadastro de robôs para automatizar tarefas do dia a dia. O objetivo é criar um código organizado e escalável, facilitando a adição de novos tipos de robôs no futuro. Para isso, é fundamental aplicar os pilares da Programação Orientada a Objetos (POO), como encapsulamento, herança e polimorfismo, garantindo que cada robô tenha suas próprias características e comportamentos, mas compartilhe uma estrutura comum. Sua missão é criar uma solução reutilizável e clara, que permita cadastrar diferentes tipos de robôs e exibir suas informações de forma padronizada.

# Implemente uma classe base chamada Robo com os atributos nome e tarefa. Em seguida, crie uma função que receba como entrada o nome e a tarefa de um robô, instancie um objeto da classe Robo e retorne uma string formatada no seguinte padrão: "Robo [nome] executa [tarefa]". Certifique-se de que a estrutura do código permita fácil extensão para novos tipos de robôs no futuro, demonstrando o uso dos conceitos fundamentais da POO.

# Entrada
# Duas strings separadas por espaço, representando respectivamente o nome do robô e a tarefa que ele executa.

# Saída
# Uma string formatada no padrão: "Robo [nome] executa [tarefa]".

class Robo:
    def __init__(self, nome: str, tarefa: str):
        self.nome = nome
        self.tarefa = tarefa

    def descricao(self) -> str:
        # TODO: Retorne a string formatada "Robo [nome] executa [tarefa]"
        return f"Robo {self.nome} executa {self.tarefa}"

def main():
    entrada = input().strip()
    partes = entrada.split(maxsplit=1)
    if len(partes) != 2:
        print("Entrada inválida")
        return
    nome, tarefa = partes
    robo = Robo(nome, tarefa)
    print(robo.descricao())

if __name__ == "__main__":
    main()