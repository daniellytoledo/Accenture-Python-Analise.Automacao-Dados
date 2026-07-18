# Manipulação de dados

# Arrays com NumPy
# Arrays são estruturas usadas para armazenar vários valores numéricos de forma eficiente.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y) # plot para criar um gráfico conectando um ponto através das duas listas
               # (1,20 | 2, 20 | 3, 25 | 4, 30)
plt.show()     # mostrar o gráfico


import pandas as pd

numeros = pd.array([1, 2, 3, 4, 5]) # o array facilita cada número ser multiplicado por 2 individualmente | chamado de operação vetorizada
resultado = numeros * 2
print(resultado)

dados = {
    "produtos": ["Notebook", "Mouse", "Teclado"],
    "preco": [3500, 120, 200]
}

df = pd.DataFrame(dados)
print(df)
#    produtos  preco
# 0  Notebook   3500
# 1     Mouse    120
# 2   Teclado    200

df.to_csv("dados.csv", index=False) # criando uma arquivo CSV de dados

leitura_df = pd.read_csv("dados.csv") # abrir o arquivo csv para visualizar o conteúdo, caso estivemos em outro código
print(leitura_df)