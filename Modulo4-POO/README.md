# 🐍 Módulo 4 — Programação Orientada a Objetos (POO) em Python

> **Bootcamp:** Accenture - Python para Análise e Automação de Dados · Plataforma DIO

---

## 📌 Sobre este módulo

Introdução aos conceitos fundamentais da Programação Orientada a Objetos em Python: classes e instâncias, construtores e destrutores, encapsulamento, herança e polimorfismo.

---

## 🗂️ Conteúdo

- [Classe e Instância](#classe-e-instância)
- [Construtores e Destrutores](#construtores-e-destrutores)
- [Encapsulamento](#encapsulamento)
- [Herança](#herança)
- [Polimorfismo](#polimorfismo)

---

## Classe e Instância

Uma **classe** é um molde que define atributos e comportamentos. Uma **instância** é um objeto concreto criado a partir desse molde, com seus próprios valores.

```python
class Pessoa:
    especie = "Homo sapiens"   # atributo de classe — compartilhado por todas as instâncias

    def __init__(self, nome, idade):
        self.nome = nome       # atributo de instância — exclusivo de cada objeto
        self.idade = idade

# Criando instâncias
pessoa1 = Pessoa("Dani", 25)
pessoa2 = Pessoa("Ana", 30)

pessoa1.nome        # "Dani"
pessoa2.nome        # "Ana"
pessoa1.especie     # "Homo sapiens" — compartilhado entre instâncias
```

> Atributos de classe são iguais para todos os objetos, enquanto atributos de instância variam de objeto para objeto.

---

## Construtores e Destrutores

O **construtor** (`__init__`) é executado automaticamente ao criar uma instância, inicializando seus atributos. O **destrutor** (`__del__`) é chamado quando o objeto é destruído ou removido da memória.

```python
class Conexao:
    def __init__(self, servidor):
        self.servidor = servidor
        print(f"Conexão com {self.servidor} aberta.")

    def __del__(self):
        print(f"Conexão com {self.servidor} encerrada.")

conexao = Conexao("banco_dados")   # "Conexão com banco_dados aberta."
del conexao                        # "Conexão com banco_dados encerrada."
```

> O destrutor é útil para liberar recursos, como fechar arquivos ou conexões, mas seu uso é menos comum em Python do que em outras linguagens, já que o coletor de lixo já gerencia boa parte da memória.

---

## Encapsulamento

Consiste em restringir o acesso direto aos atributos de um objeto, protegendo os dados internos e expondo apenas o necessário por meio de métodos.

```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo     # atributo privado (prefixo __)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria("Dani", 1000)
conta.depositar(500)
conta.consultar_saldo()      # 1500

conta.__saldo                # ❌ AttributeError — acesso direto bloqueado
```

| Prefixo | Nível de acesso |
|---------|------------------|
| `atributo` | Público — acesso livre |
| `_atributo` | Protegido — convenção, uso interno recomendado |
| `__atributo` | Privado — acesso restrito via *name mangling* |

> O encapsulamento evita que dados internos sejam alterados de forma inconsistente fora da classe.

---

## Herança

Permite que uma classe (filha) herde atributos e métodos de outra classe (mãe), reaproveitando código e criando relações de especialização.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f"{self.nome} faz um som.")

class Cachorro(Animal):          # herda de Animal
    def fazer_som(self):
        print(f"{self.nome} late: Au au!")

class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} mia: Miau!")

rex = Cachorro("Rex")
rex.fazer_som()       # "Rex late: Au au!"

# Reutilizando o método da classe mãe com super()
class Filhote(Cachorro):
    def __init__(self, nome, idade):
        super().__init__(nome)
        self.idade = idade
```

> `super()` permite acessar métodos da classe mãe dentro da classe filha, evitando reescrever código já existente.

---

## Polimorfismo

Permite que classes diferentes respondam de forma distinta a uma mesma chamada de método, cada uma seguindo sua própria implementação.

```python
animais = [Cachorro("Rex"), Gato("Miau")]

for animal in animais:
    animal.fazer_som()
# "Rex late: Au au!"
# "Miau mia: Miau!"
```

O mesmo método `fazer_som()` é chamado para todos os objetos, mas o comportamento muda de acordo com a classe de cada instância.

```python
# Polimorfismo também ocorre com funções built-in do Python
len("Python")     # 6      — tamanho da string
len([1, 2, 3])    # 3      — tamanho da lista
len({"a": 1})     # 1      — número de chaves do dicionário
```

> O polimorfismo torna o código mais flexível e extensível, permitindo tratar objetos de tipos diferentes de forma uniforme.

---

## 🛠️ Tecnologias utilizadas neste módulo

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Claude](https://img.shields.io/badge/Anthropic-Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-README-000000?style=for-the-badge&logo=markdown&logoColor=white)

---

*Documentação gerada como parte do Bootcamp Accenture - Python para Análise e Automação de Dados · Plataforma DIO*