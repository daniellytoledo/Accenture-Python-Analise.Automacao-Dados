import pandas as pd

df = pd.read_csv("dados.csv")

print(df["preco"])

print(df["preco"].mean()) # mean() calcula a média da coluna selecionada que neste caso é o preço

print(df["produtos"].count()) # count() para contar quantos registros tem na coluna produtos

print(df.describe())
#              preco
# count     3.000000   - quantos registros tem na coluna preco
# mean   1273.333333   - a média da coluna
# std    1928.764717   - desvio padrão
# min     120.000000   - o valor mínimo
# 25%     160.000000   - 1º quartil, 25% dos dados estão abaixo desse valor
# 50%     200.000000   - 2º quartil, 50% dos dados estão abaixo desse valor
# 75%    1850.000000   - 3º quartil, 75% dos dados estão abaixo desse valor
# max    3500.000000   - maior valor

df.info()
# O método df.info() mostra um resumo do DataFrame, informando quantas linhas ele possui, os tipos de dados de cada coluna, se existem valores nulos e quanta memória está sendo utilizada.

# <class 'pandas.DataFrame'>               - Mostra o tipo do objeto. df é um DataFrame
# RangeIndex: 3 entries, 0 to 2            - Significa que o DataFrame possui 3 linhas.
# Data columns (total 2 columns):          - Informa que existem 2 colunas.
# #   Column    Non-Null Count  Dtype      - É o nome da coluna exibida.
# 0   produtos  3 non-null      str        - Mostra quantos valores não são nulos.
# 1   preco     3 non-null      int64      - Isso indica que apenas 3 das 3 linhas possuem valor.
# dtypes: int64(1), str(1)                 - Mostra o tipo dos dados da coluna. uma é inteiro e a outra é string neste caso
# memory usage: 180.0 bytes                - Mostra aproximadamente quanta memória o DataFrame ocupa na RAM.