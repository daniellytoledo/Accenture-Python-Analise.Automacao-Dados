# Storytelling com Dados
# Storytelling com dados significa usar visualizações para contar uma história. O objetivo não é apenas mostrar gráficos, mas comunicar insights. Um bom storytelling deve:

# mostrar o contexto
# destacar padrões
# explicar resultados

# ------------------------------------------------------------------------------------------------

# Avançando na visualização interativa com Plotly
# Gráficos interaitvos permitem explorar os dados de forma dinâmica. O usuário pode:

# passar o mouse sobre os pontos
# filtrar
# analisar padrões rapidamente

import pandas as pd
import plotly.express as px

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url) # transforma os dados em uma tabela guardando os dados em uma DataFrame chamada df

# gráfico plotly interativo, quando se coloca o mouse em cima das bolinhas do gráfico, aparece as informações que estão definidas em fig como o sexo, a hora, o tamanho da bolinha, valores
fig = px.scatter(                                 
    df,
    x="total_bill",
    y="tip",
    color="day",
    size="size",
    hover_data=["sex", "time"],
    title="Relação entre conta e gorjeta"
)

fig.show()

#--------------------------------------------------------------------------------------------

# Heatmap de Correlação
# Um heatmap mostra a relação entre variáveis numéricas. Ele ajuda a identificar padrões e correlações.

import seaborn as sns
import matplotlib.pyplot as plt

# esse gráfico mostra a relação entre as variáveis numéricas, neste caso se compara size, total_bill e tip.
# o gráfico mostra a relação de 0 até 1, sendo 1 a mais forte correlação.
# além disso, as cores mais quentes significa uma correlação mais forte, sendo mais próximo de 1, e tons frios significa correlações mais fracas
# esse tipo de gráfico é usado quando se quer avalisar várias variáveis ao mesmo tempo

correlacao = df.corr(numeric_only=True)
plt.figure(figsize=(8,6))

sns.heatmap(
    correlacao,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlação entre variáveis")
plt.show()

