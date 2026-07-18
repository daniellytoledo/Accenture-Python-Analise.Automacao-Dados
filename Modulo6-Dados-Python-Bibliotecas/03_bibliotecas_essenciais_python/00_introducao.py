# Introdução às bibliotecas de dados

# O Python possui muitas bibliotecas para trabalhar com dados. As três bibliotecas mais utilizadas são:

# NumPy      - computação numérica e arrays
# NumPy é muito usado para trabalhar com arrays e operações matemáticas eficientes. Ela é muito mais rápida que listas comuns no Python apra operações numéricas.

# Pandas     - manipulação de dados em tabelas
# Pandas é usado para manipular dados estruturados, como tabelas. A principal estrutura de dados é o DataFrame, que funciona como uma planilha. O pandas permite ler arquivos como CSV, Excel, JSON...

# Matplotlib - criação de gráficos
# Matplotlib é uma biblioteca usada para criar gráficos e visualizações de dados.

import numpy as np        # podemos abreviar cada biblioteca usando o AS 
import pandas as pd       # pois ao trabalhar com dados podemos ter que mencionar
import matplotlib.pyplot as plt  # a biblioteca várias vezes, então assim fica mais fácil

# NumPy -------------------------------------------

array = np.array([1, 2, 3, 4, 5])
print(array) # [1 2 3 4 5]

# Pandas ------------------------------------------

dados = {
    "nome": ["Ana", "Carlos", "Maria"],
    "idade": [25, 30, 28]
}

df = pd.DataFrame(dados) # Pandas.DataFrame para organizar os dados em tabela
print(df)
#      nome  idade
# 0     Ana     25
# 1  Carlos     30
# 2   Maria     28

# Matplotlib --------------------------------------

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()