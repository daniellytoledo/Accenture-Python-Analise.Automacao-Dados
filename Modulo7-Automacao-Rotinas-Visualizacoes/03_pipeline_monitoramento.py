# Projeto prático de automação
# O que é um pipeline de dados?
# Um pipeline de dados é um processo automatizado que executa várias etapas:

# 1º coleta de dados
# 2º processamento
# 3º análise
# 4º geração de resultados

# Pipeline são muitos usados em:

# análise de dados
# engenharia de dados
# relatórios automáticos

# Dataset real utilizado

# Vamos utilizar um dataset real de vendas de e-commerce
# Esse dataset contém:
# produtos vendidos, quantidade, preço, país de venda

import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)
df.head()

# Processamento automático dos dados

total_gorjetas = df["tip"].sum()
print("Total das gorjetas: ", total_gorjetas)

gorjetas_por_dia = df.groupby("day")["tip"].sum()
print(gorjetas_por_dia)
# day
# Fri      51.96
# Sat     260.40
# Sun     247.39
# Thur    171.83

# Criando um pipeline automatizado usando função def

def pipeline_restaurante():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv" # coleta os dados
    df = pd.read_csv(url)                      # carrega os dados
    total_gorjetas = df["tip"].sum()           # faz uma análise de dados, somando todas as gorjetas
    
    relatorio = pd.DataFrame({                 # cria um DataFrame apenas com o total de gorjetas
        "total_gorjetas":[total_gorjetas]
    })

    relatorio.to_csv("relatorio_gorjetas.csv", index=False) # cria um arquivo relatorio_gorjetas.csv

    print("Pipeline executado com sucesso.")
    print("Total de gorjetas:", total_gorjetas)

pipeline_restaurante()

