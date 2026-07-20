# Tratamento de valores ausentes

# O que é NaN?
# NaN significa Not a Number. Ele representa valores ausentes ou desconhecidos em um dataset.

import pandas as pd

url ="https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"

df = pd.read_csv(url)

# podemos usar a função isnull() para sabermos quais colunas possuem dados vazios, dando resultados True ou False
# a função sum() pode ser usada junto com a função para somar as linhas vazias em cada coluna

print(df.isnull().sum()) 

# PassengerId      0
# Survived         0
# Pclass           0
# Name             0
# Sex              0
# Age            177
# SibSp            0
# Parch            0
# Ticket           0
# Fare             0
# Cabin          687
# Embarked         2
# dtype: int64

# --------------------------------------------------------------------------------------

# Remoção de valores ausentes
# a função dropna() remove todas as linhas que possuem valores ausentes
df.limpo = df.dropna()

# às vezes, as linhas são tão importantes, que a solução não é removê-las e sim substituir os valores vazios pela média, mediana daquele valor das outras linhas ou valores mais comuns. (ou até usar outra estratégia)

# Preenchimento de valores ausentes
# Em vez de remover dados, podemos preencher os valores faltantes.
# nesse código abaixo, selecionamos a coluna Age, usamos a função fillna() para preencher df["Age"] com a média disponível na coluna Age, então tudo que está vazio vai ser substituído pela média das outras linhas
df["Age"] = df["Age"].fillna(df["Age"].mean()) 

# Para verificar quantos valores ausentes existem na coluna Age
df["Age"].isnull().sum()