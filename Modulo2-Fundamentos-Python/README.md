# 🐍 Módulo 2 — Conhecendo a Linguagem de Programação Python

> **Bootcamp:** Accenture - Python para Análise e Automação de Dados · Plataforma DIO

---

## 📌 Sobre este módulo

Introdução à linguagem Python com foco nos fundamentos essenciais para análise de dados: tipos de dados, operadores, estruturas de controle e manipulação de strings.

---

## 🗂️ Conteúdo

- [Tipos de Dados](#tipos-de-dados)
- [Modo Interativo no Terminal](#modo-interativo-no-terminal)
- [Variáveis e Constantes](#variáveis-e-constantes)
- [Conversão de Tipos](#conversão-de-tipos)
- [Funções de Entrada e Saída](#funções-de-entrada-e-saída)
- [Operadores Aritméticos](#operadores-aritméticos)
- [Operadores de Comparação](#operadores-de-comparação)
- [Operadores de Atribuição](#operadores-de-atribuição)
- [Operadores Lógicos](#operadores-lógicos)
- [Operadores de Identidade](#operadores-de-identidade)
- [Operadores de Associação](#operadores-de-associação)
- [Indentação e Blocos](#indentação-e-blocos)
- [Estruturas Condicionais](#estruturas-condicionais)
- [Estruturas de Repetição](#estruturas-de-repetição)
- [Métodos Úteis da Classe String](#métodos-úteis-da-classe-string)
- [Interpolação de Variáveis](#interpolação-de-variáveis)
- [Fatiamento de String](#fatiamento-de-string)
- [Strings Múltiplas Linhas](#strings-múltiplas-linhas)

---

## Tipos de Dados

Python é uma linguagem de tipagem dinâmica — o tipo é inferido automaticamente no momento da atribuição.

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `int` | Número inteiro | `10`, `-3` |
| `float` | Número decimal | `3.14`, `-0.5` |
| `bool` | Booleano | `True`, `False` |
| `str` | Texto | `"Python"` |
| `list` | Lista mutável | `[1, 2, 3]` |
| `tuple` | Lista imutável | `(1, 2, 3)` |
| `dict` | Dicionário chave-valor | `{"nome": "Ana"}` |
| `None` | Ausência de valor | `None` |

```python
tipo = type(42)      # <class 'int'>
tipo = type("olá")   # <class 'str'>
tipo = type(3.14)    # <class 'float'>
```

---

## Modo Interativo no Terminal

O modo interativo permite executar comandos Python linha a linha diretamente no terminal, sem criar um arquivo. Útil para testes rápidos e exploração.

```bash
# Iniciar o modo interativo
python3

# Sair do modo interativo
exit()
```

```python
# Exemplo de uso no modo interativo
>>> 2 + 2
4
>>> nome = "Dani"
>>> print(f"Olá, {nome}!")
Olá, Dani!
```

> O símbolo `>>>` indica que o interpretador está aguardando um comando.

---

## Variáveis e Constantes

**Variáveis** armazenam valores que podem ser alterados. Em Python, não é necessário declarar o tipo.

```python
nome = "Dani"
idade = 25
altura = 1.68
```

**Constantes** são convencionalmente escritas em letras maiúsculas. Python não possui constantes nativas — é uma convenção para indicar que o valor não deve ser alterado.

```python
PI = 3.14159
TAXA_JUROS = 0.05
```

> Por convenção, use `snake_case` para variáveis e `UPPER_CASE` para constantes.

---

## Conversão de Tipos

Permite transformar um tipo de dado em outro. Também chamada de *type casting*.

```python
# Conversão explícita
int("10")        # 10  (str → int)
float("3.14")    # 3.14 (str → float)
str(100)         # "100" (int → str)
bool(0)          # False
bool(1)          # True

# Cuidado com conversões inválidas
int("abc")       # ❌ ValueError
```

---

## Funções de Entrada e Saída

**Saída — `print()`:** exibe informações na tela.

```python
print("Olá, mundo!")
print("Nome:", "Dani", sep=" | ")   # separador personalizado
print("Linha 1", end=" ")           # substitui a quebra de linha padrão
print("Linha 2")                    # resultado: Linha 1 Linha 2
```

**Entrada — `input()`:** captura dados digitados pelo usuário. Sempre retorna `str`.

```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))  # conversão necessária para int
```

---

## Operadores Aritméticos

| Operador | Operação | Exemplo | Resultado |
|----------|----------|---------|-----------|
| `+` | Adição | `5 + 3` | `8` |
| `-` | Subtração | `5 - 3` | `2` |
| `*` | Multiplicação | `5 * 3` | `15` |
| `/` | Divisão | `5 / 2` | `2.5` |
| `//` | Divisão inteira | `5 // 2` | `2` |
| `%` | Módulo (resto) | `5 % 2` | `1` |
| `**` | Exponenciação | `2 ** 3` | `8` |

---

## Operadores de Comparação

Retornam sempre `True` ou `False`.

| Operador | Significado | Exemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Maior que | `5 > 3` | `True` |
| `<` | Menor que | `5 < 3` | `False` |
| `>=` | Maior ou igual | `5 >= 5` | `True` |
| `<=` | Menor ou igual | `3 <= 5` | `True` |

---

## Operadores de Atribuição

| Operador | Equivale a | Exemplo |
|----------|------------|---------|
| `=` | Atribuição simples | `x = 10` |
| `+=` | `x = x + n` | `x += 5` |
| `-=` | `x = x - n` | `x -= 5` |
| `*=` | `x = x * n` | `x *= 2` |
| `/=` | `x = x / n` | `x /= 2` |
| `//=` | `x = x // n` | `x //= 2` |
| `%=` | `x = x % n` | `x %= 3` |
| `**=` | `x = x ** n` | `x **= 2` |

---

## Operadores Lógicos

Combinam expressões booleanas.

| Operador | Descrição | Exemplo | Resultado |
|----------|-----------|---------|-----------|
| `and` | Verdadeiro se ambos forem verdadeiros | `True and False` | `False` |
| `or` | Verdadeiro se ao menos um for verdadeiro | `True or False` | `True` |
| `not` | Inverte o valor booleano | `not True` | `False` |

```python
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
```

---

## Operadores de Identidade

Verificam se dois objetos ocupam o **mesmo espaço na memória** — não apenas se têm o mesmo valor.

| Operador | Descrição |
|----------|-----------|
| `is` | Retorna `True` se forem o mesmo objeto |
| `is not` | Retorna `True` se **não** forem o mesmo objeto |

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

a is b      # True  — mesma referência na memória
a is c      # False — valores iguais, mas objetos diferentes
a is not c  # True
```

---

## Operadores de Associação

Verificam se um valor está **contido** em uma sequência (string, lista, tupla, etc.).

| Operador | Descrição |
|----------|-----------|
| `in` | Retorna `True` se o valor estiver na sequência |
| `not in` | Retorna `True` se o valor **não** estiver na sequência |

```python
frutas = ["maçã", "banana", "uva"]

"banana" in frutas      # True
"manga" not in frutas   # True

"Py" in "Python"        # True
```

---

## Indentação e Blocos

Python usa **indentação** (espaços ou tabulação) para definir blocos de código — não usa chaves `{}` como outras linguagens. O padrão recomendado é **4 espaços**.

```python
# Correto
if True:
    print("Dentro do bloco")   # 4 espaços
    print("Ainda no bloco")

print("Fora do bloco")

# Incorreto — IndentationError
if True:
print("Sem indentação")   # ❌
```

> Misturar espaços e tabulações causa erros. Escolha um padrão e mantenha consistência em todo o projeto.

---

## Estruturas Condicionais

Permitem executar blocos de código com base em condições.

```python
# if / elif / else
nota = 7.5

if nota >= 9:
    print("Aprovado com distinção")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")
```

**Condicional ternária** — forma resumida para condições simples:

```python
status = "maior" if idade >= 18 else "menor"
```

---

## Estruturas de Repetição

**`for`** — itera sobre uma sequência.

```python
frutas = ["maçã", "banana", "uva"]

for fruta in frutas:
    print(fruta)

# Com range
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)
```

**`while`** — repete enquanto a condição for verdadeira.

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

**Comandos auxiliares:**

```python
break       # encerra o loop imediatamente
continue    # pula para a próxima iteração
```

---

## Métodos Úteis da Classe String

```python
texto = "  Olá, Mundo!  "

texto.upper()           # "  OLÁ, MUNDO!  "
texto.lower()           # "  olá, mundo!  "
texto.strip()           # "Olá, Mundo!"      — remove espaços nas bordas
texto.lstrip()          # "Olá, Mundo!  "    — remove espaços à esquerda
texto.rstrip()          # "  Olá, Mundo!"    — remove espaços à direita
texto.replace("Mundo", "Python")  # "  Olá, Python!  "
texto.split(",")        # ['  Olá', ' Mundo!  ']
texto.strip().startswith("Olá")   # True
texto.strip().endswith("!")       # True
texto.strip().find("Mundo")       # 5  — índice da primeira ocorrência
"Python".center(10, "-")          # "--Python--"
"  ".isspace()                    # True
"123".isnumeric()                 # True
```

---

## Interpolação de Variáveis

Formas de inserir variáveis dentro de strings.

```python
nome = "Dani"
idade = 25

# f-string (recomendada — Python 3.6+)
print(f"Nome: {nome}, Idade: {idade}")

# .format()
print("Nome: {}, Idade: {}".format(nome, idade))
print("Nome: {n}, Idade: {i}".format(n=nome, i=idade))

# % (antiga, menos usada)
print("Nome: %s, Idade: %d" % (nome, idade))
```

> **f-string** é a forma mais moderna, legível e performática. Prefira sempre que possível.

---

## Fatiamento de String

Permite extrair partes de uma string usando a sintaxe `[início:fim:passo]`.

```python
texto = "Python"
#         0 1 2 3 4 5   (índices positivos)
#        -6-5-4-3-2-1   (índices negativos)

texto[0]        # "P"
texto[-1]       # "n"
texto[0:3]      # "Pyt"   — do índice 0 até 2 (fim não incluso)
texto[2:]       # "thon"  — do índice 2 até o fim
texto[:4]       # "Pyth"  — do início até o índice 3
texto[::-1]     # "nohtyP" — string invertida
texto[::2]      # "Pto"   — um caractere sim, um não
```

---

## Strings Múltiplas Linhas

Usam **três aspas** (`"""` ou `'''`) para definir textos com quebras de linha.

```python
mensagem = """
Olá, seja bem-vindo!
Este é um texto
com múltiplas linhas.
"""

print(mensagem)
```

Muito úteis para docstrings (documentação de funções e classes):

```python
def calcular_media(notas):
    """
    Calcula a média de uma lista de notas.

    Parâmetros:
        notas (list): lista de valores numéricos

    Retorna:
        float: média aritmética das notas
    """
    return sum(notas) / len(notas)
```

---

## 🛠️ Tecnologias utilizadas neste módulo

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-README-000000?style=for-the-badge&logo=markdown&logoColor=white)

---

*Documentação gerada como parte do Bootcamp Accenture — Python para Análise e Automação de Dados · DIO*