# Automação de Pré-Processamento

# Pipelines de dados
# Um pipeline de dados executa várias etapas automaticamente.
# 1. carregar dados
# 2. limpar dados
# 3. transformar dados
# 4. gerar dataset final

# Exemplo:

import pandas as pd

url ="https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"

df = pd.read_csv(url) # ler o arquivo

# função que recebe o DataFrame df como parametro para executar a primeira limpeza
# a primeira linha da função substitui as linhas vazias (NaN) em Age pela média de todos os valores da coluna
# o inplace=True diz para que o código altere os dados diretamente na coluna original
# já na segunda linha, é criado uma nova coluna chamada Fare_normalized usando a técnica Min-Máx Scalin
# criar essa função é uma maneira de automatizar a limpeza de dados chamando a função limpar_dados() sem precisar repetir código
# podemos chamar esse processo também de pipeline de pré-processamento

def limpar_dados(df):
    df["Age"].fillna(df["Age"].mean(), inplace=True)

    df["Fare_normalized"] = (
        df["Fare"] - df["Fare"].min()
    ) / (df["Fare"].max() - df["Fare"].min())

    return df

# depois dessa primeira parte com a pipeline, vamos falar sobre Documentação e Validação

# Reprodutividade

# Uma análise deve ser reproduzível. Isso significa que qualquer pessoa deve conseguir executar o código e obter os mesmos resultados.

# Validação de Datasets

# Antes de usar um dataset, devemos verificar:
# valores ausentes
# tipos de dados
# consistência

def validar_dataset(df):
    print("Linhas:", df.shape[0])   # retorna a quantidade do dataset
    print("Colunas:", df.shape[1])  # indica as colunas
    print("\n Valores ausentes: ") 
    print(df.isnull().sum())        # exibe a quantidade de valores ausentes em cada coluna

validar_dataset(df)
# Linhas: 891
# Colunas: 12

# Valores ausentes: 
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

# Com esse resultado, podemos ver que as colunas Cabin, Age e Embarked ainda possuem valores vazios
# Ao analisar que ainda possuem colunas com valores vazios, é importante verificar se essas informações são importantes para determinada análise, e aí pensar em qual a melhor forma tratar e se faz sentido

