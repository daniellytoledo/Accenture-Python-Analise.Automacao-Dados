# Introdução às boas práticas
# O que é clean code?

# Clean Code significa escrever código que seja:

# fácil de ler
# fácil de entender
# fácil de manter

# Um bom código não é apenas funcional, ele também é organizado e claro.

#------------------------------------------------------------------------------------------------

# Exemplo ruins:

# 1. nesse exemplo temos 3 variáveis, mas as variáveis não diz nada. não sabemos o que é x, o que é y ou o que representa o valor de z, qual o objetivo dessa conta, ou seja:
# não tem contexto
# não é descritivo
# não comunica a intenção da análise
x = 10
y = 20
z = x + y
print(z)

# uma pequena melhorada, porém ainda não ideal
numero1 = 10
numero2 = 20
soma    = numero1 + numero2
print(soma)

#------------------------------------------------------------------------------------------------

# Regras Importantes

# Nomes claros
# Funções pequenas
# Evitar "mágica" no código
# Comentar apenas quando necessário

# Organização, Estrutura de Pastas
# Projetos organizados facilitam a manutenção. Exemplo de estrutura:

# projeto/
# │
# ├── src/
# │   ├── main.py
# │   ├── utils.py
# │
# ├── tests/
# │   test.utils.py
# │
# ├── data/
# │   requirements.txt

#-----------------------------------------------------------------------------------------

# Modularização
# Separar responsabilidades:
# cálculo  -> utils.py
# execução -> main.py
# testes   -> tests/

# Função em módulo separado

def calcular_soma(a,b):
    return a+b

# uso da função
resultado = calcular_soma(10,5)
print(resultado)

# Em análise de dados, podemos ter função para limpar dados, calcular receita, normalizar valores, e o pipeline vai apenas orquestrar essas tarefas.