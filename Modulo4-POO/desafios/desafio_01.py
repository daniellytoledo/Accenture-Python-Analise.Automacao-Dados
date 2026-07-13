# Desafio

# Você foi contratado por uma consultoria de TI para ajudar a modelar o sistema de cadastro de clientes de uma empresa fictícia chamada TechBiz. O objetivo é criar uma estrutura que represente clientes utilizando classes e objetos, facilitando a manipulação das informações de cada cliente. O sistema precisa ser simples, mas robusto o suficiente para identificar clientes VIPs, que são aqueles cujo saldo é igual ou superior a 1000 unidades. Sua tarefa é implementar uma classe que represente um cliente, armazenando nome, email e saldo. Em seguida, você deve criar um objeto dessa classe a partir dos dados fornecidos e informar se o cliente é VIP ou não, de acordo com a regra de negócio estabelecida.

# Implemente a classe Cliente com os atributos nome, email e saldo. Após criar o objeto Cliente com os dados recebidos, verifique se o saldo é igual ou maior que 1000. Se for, imprima "VIP"; caso contrário, imprima "REGULAR". Não utilize bibliotecas externas. O programa deve ser implementado em um único arquivo.

# Entrada
# Três linhas, cada uma contendo respectivamente: o nome do cliente (string), o email do cliente (string) e o saldo do cliente (inteiro não negativo).

# Saída
# Uma única linha contendo "VIP" se o saldo for igual ou superior a 1000, ou "REGULAR" caso contrário.

class Cliente:
    def __init__(self, nome: str, email: str, saldo: int):
        self.nome = nome
        self.email = email
        self.saldo = saldo

    def is_vip(self) -> bool:
        # TODO: Retorne True se o saldo for igual ou maior que 1000, senão False
        return self.saldo >= 1000

# Entrada: nome, email e saldo do cliente (um por linha)
nome = input()
email = input()
saldo = int(input())

cliente = Cliente(nome, email, saldo)

# Saída: imprima "VIP" se o cliente for VIP, senão "REGULAR"
if cliente.is_vip():
    print("VIP")
else:
    print("REGULAR")