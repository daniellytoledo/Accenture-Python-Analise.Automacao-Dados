# Introdução à Visualização de Dados

# Importância da visualização de dados
# A visualização de dados permite transformar informações em gráficos fáceis de interpretar. Com gráficos podemos:

# identificar padrões
# comparar valores
# detectar tendências
# comunicar resultados de forma clara

# Por isso a visualização é uma etapa essencial na análise de dados

# Dataset utilizado

# Vamos usar um dataset real com dados de gorjetas em restaurantes. O dataset contém:

# valor da conta
# valor da gorjeta
# dia da semana
# número de pessoas
# horário da refeição

import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url) # transforma os dados em uma tabela guardando os dados em uma DataFrame chamada df
df.head()             # mostra as 5 primeiras linhas da tabela. o valor 5 é default


# Python possui várias bibliotecas para visualização de dados. Algumas das mais utilizadas são:

# Matplotlib   - gráficos básicos
# Seaborn      - gráficos estatísticos
# Plotly       - gráficos interativos

import matplotlib.pyplot as plt

plt.scatter(df["total_bill"], df["tip"]) # cria um gráfico de dispersão x, y pra mostrar a relação entre duas variáveis (valor da conta e o valor da gorjeta)
# a análise dos dados nesse caso é que o valor da gorjeta é sempre maior com os gastos maiores de conta

plt.xlabel("Contal Total")               # título do eixo x
plt.ylabel("Valor da gorjeta")           # título do eixo y

plt.title("Relação conta e gorjeta")     # título do gráfico

plt.show()

#-----------------------------------------------------------------------------------------------

import seaborn as sns

sns.scatterplot(data=df, x="total_bill", y="tip")  # também é um gráfico de dispersão e a interpretação é a mesma
plt.show()

#-----------------------------------------------------------------------------------------------

import plotly.express as px

# também é um gráfico de dispersão, porém podemos colocar cores pra separar categorias
# nesse caso as cores estão especificando os dias de cada conta conta e gorjea
fig = px.scatter(                                 
    df,
    x="total_bill",
    y="tip",
    color="day",
    title="Relação entre conta e gorjeta"
)

fig.show()

#------------------------------------------------------------------------------------------------

# A personalização permite melhorar a apresentação dos gráficvos. Podemos alterar: cores, estilos, títulos, layouts.

# gráfico de barras na cor verde. Gráfico de barras serve para comparar categorias
plt.figure(figsize=(8,5))
plt.bar(df["day"], df["tip"], color="green") 
plt.title("Gorjetas por dia")

plt.xlabel("Dia")
plt.ylabel("Gorjeta")

plt.show()

#--------------------------------------------------------------------------------------------------

fig, ax = plt.subplots(1, 2, figsize=(10,4))

# gráfico histograma para entender a distribuição de uma variável
sns.histplot(df["total_bill"], ax=ax[0])
ax[0].set_title("Distribuição da Conta")

# gráfico boxe plot para entender a distribuição entre categorias
sns.boxenplot(data=df, x="day", y="tip", ax=ax[1])
ax[1].set_title("Gorjetas por Dia")

plt.show()
