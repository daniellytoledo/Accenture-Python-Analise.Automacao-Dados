# 🐍 Módulo 3 — Manipulação de Dados com Estruturas Fundamentais em Python

> **Bootcamp:** Accenture - Python para Análise e Automação de Dados · Plataforma DIO

---

## 📌 Sobre este módulo

Aprofundamento em Python com foco nas estruturas de dados fundamentais para manipulação e organização da informação: listas, tuplas, conjuntos, dicionários e funções.

---

## 🗂️ Conteúdo

- [Listas](#listas)
- [Tuplas](#tuplas)
- [Conjuntos (Sets)](#conjuntos-sets)
- [Dicionários](#dicionários)
- [Funções](#funções)

---

## Listas

Estrutura de dados **mutável** e **ordenada**, capaz de armazenar múltiplos valores — inclusive de tipos diferentes — em uma única variável. É uma das estruturas mais usadas em Python por sua flexibilidade.

```python
frutas = ["maçã", "banana", "uva"]

# Acessando elementos
frutas[0]          # "maçã"
frutas[-1]         # "uva"

# Modificando
frutas[1] = "pera"
frutas.append("manga")        # adiciona ao final
frutas.insert(0, "abacaxi")   # insere em posição específica
frutas.remove("uva")          # remove pelo valor
frutas.pop()                  # remove e retorna o último item
frutas.sort()                 # ordena a lista
frutas.reverse()              # inverte a ordem

# Fatiamento (slicing)
frutas[1:3]        # sublista do índice 1 ao 2

# List comprehension
quadrados = [n**2 for n in range(5)]   # [0, 1, 4, 9, 16]
```

> Listas são ideais quando os dados podem mudar ao longo da execução do programa.

---

## Tuplas

Estrutura de dados **imutável** e **ordenada**. Uma vez criada, seus valores não podem ser alterados — o que garante mais segurança e desempenho em relação às listas.

```python
coordenadas = (10, 20)
cores = ("vermelho", "verde", "azul")

# Acessando elementos
cores[0]           # "vermelho"
cores[-1]           # "azul"

# Desempacotamento (unpacking)
x, y = coordenadas
print(x, y)         # 10 20

# Tupla com um único elemento (necessita da vírgula)
unica = (1,)

# Tentativa de alteração gera erro
cores[0] = "amarelo"   # ❌ TypeError
```

> Use tuplas para dados que não devem ser modificados, como coordenadas, configurações fixas ou registros constantes.

---

## Conjuntos (Sets)

Estrutura de dados **mutável**, **não ordenada** e que **não permite elementos duplicados**. Muito útil para operações matemáticas de conjuntos e para eliminar repetições.

```python
numeros = {1, 2, 3, 3, 2}    # {1, 2, 3} — duplicados são removidos automaticamente

# Adicionando e removendo
numeros.add(4)
numeros.remove(1)

# Operações entre conjuntos
a = {1, 2, 3}
b = {2, 3, 4}

a.union(b)          # {1, 2, 3, 4}        — união
a.intersection(b)   # {2, 3}              — interseção
a.difference(b)     # {1}                 — diferença
a.symmetric_difference(b)  # {1, 4}       — elementos exclusivos de cada um

# Verificando pertencimento
2 in a               # True
```

> Como não possuem ordem definida, sets não suportam indexação (`numeros[0]` gera erro).

---

## Dicionários

Estrutura de dados **mutável** que armazena valores em pares de **chave-valor**. Permite acesso rápido aos dados por meio de uma chave única, em vez de um índice numérico.

```python
pessoa = {
    "nome": "Dani",
    "idade": 25,
    "cidade": "Faro"
}

# Acessando valores
pessoa["nome"]              # "Dani"
pessoa.get("idade")         # 25
pessoa.get("email", "não informado")   # valor padrão se a chave não existir

# Modificando
pessoa["idade"] = 26
pessoa["profissao"] = "Analista de Dados"   # adiciona nova chave

# Removendo
pessoa.pop("cidade")

# Iterando
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

pessoa.keys()        # todas as chaves
pessoa.values()       # todos os valores

# Dict comprehension
quadrados = {n: n**2 for n in range(5)}   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

> Dicionários são ideais para representar registros com atributos nomeados, como um objeto JSON.

---

## Funções

Blocos de código reutilizáveis que executam uma tarefa específica. Ajudam a organizar o código, evitar repetição e facilitar manutenção.

```python
# Função simples
def saudacao(nome):
    return f"Olá, {nome}!"

saudacao("Dani")     # "Olá, Dani!"

# Parâmetro com valor padrão
def saudacao(nome="visitante"):
    return f"Olá, {nome}!"

saudacao()            # "Olá, visitante!"

# Múltiplos retornos
def calcular(a, b):
    return a + b, a - b, a * b

soma, subtracao, multiplicacao = calcular(10, 5)

# *args — número variável de argumentos posicionais
def somar_tudo(*numeros):
    return sum(numeros)

somar_tudo(1, 2, 3, 4)   # 10

# **kwargs — número variável de argumentos nomeados
def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_dados(nome="Dani", idade=25)

# Funções lambda (anônimas)
dobro = lambda x: x * 2
dobro(5)              # 10
```

> Funções tornam o código mais legível e testável — cada função deve, idealmente, ter uma única responsabilidade.

---

## 🛠️ Tecnologias utilizadas neste módulo

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-README-000000?style=for-the-badge&logo=markdown&logoColor=white)

---

*Documentação gerada como parte do Bootcamp Accenture — Python para Análise e Automação de Dados · DIO*