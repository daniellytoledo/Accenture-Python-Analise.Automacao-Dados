# Normalização e Padronização

# Transformação de Variáveis
# Às vezes precisamos transformar dados para facilitar a análise. 

import pandas as pd

url ="https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"

df = pd.read_csv(url)

# aqui estamos criando uma coluna nova chamada Age_log com as mesmas informações da coluna original Age, usando a função apply() para aplicar os dados e lambda para copiar os dados
# isso permite adaptar as variáveis para que elas sejam mais adequadas para análise

df["Age_log"] = df["Age"].apply(lambda x: x)

# --------------------------------------------------------------------------------------

# Escala de dados
# Em alguns casos precisamos colocar os dados na mesma escala.

# Técnica min max scaling, que transforma os valores entre 0 e 1.
# Ela é muito utilizada em Machine Learning, pois alguns algoritmos funcionam melhor quando todas as variáveis têm a mesma escala.
# Essa técnica utiliza uma fórmula que pega o valor original, subtrai o valor minimo da coluna, divide pelo intervalo entre o valor máximo e o valor mínimo.
# Criando uma coluna nova chamada de Fare Normalized
# Serve para colocar todas as variáveis em uma escala semelhante para melhorar a análise

df["Fare_normalized"] = (df["Fare"] - df["Fare"].min()) / (df["Fare"].max() - df["Fare"].min())

