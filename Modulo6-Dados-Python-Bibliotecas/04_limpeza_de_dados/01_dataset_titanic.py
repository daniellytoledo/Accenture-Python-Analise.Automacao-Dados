import pandas as pd

url ="https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"

df = pd.read_csv(url)


# 1º Um dos primeiros passos para uma análise de dados é usar a função head()
# head() mostra apenas as primeiras linhas do DataFrame, só pra visualizar a estrutura sem ler o arquivo inteiro
print(df.head())

# ---------------------------------------------------------------------------------------------

# 2º Um segundo passo é usar info() para sabermos um resumo geral da estrututra do DataFrame

print(df.info())

# <class 'pandas.DataFrame'>
# RangeIndex: 891 entries, 0 to 890         - aqui se percebe que a tabela tem 891 linhas
# Data columns (total 12 columns):
# #   Column       Non-Null Count  Dtype  
# ---  ------       --------------  -----  
# 0   PassengerId  891 non-null    int64  
# 1   Survived     891 non-null    int64  
# 2   Pclass       891 non-null    int64  
# 3   Name         891 non-null    str    
# 4   Sex          891 non-null    str    
# 5   Age          714 non-null    float64   - 714 linhas com dados sobre idade, já nos mostra que há espaços vazios
# 6   SibSp        891 non-null    int64  
# 7   Parch        891 non-null    int64  
# 8   Ticket       891 non-null    str    
# 9   Fare         891 non-null    float64
# 10  Cabin        204 non-null    str       - assim como a cabine, apenas 204 linhas foram preenchidas
# 11  Embarked     889 non-null    str    
# dtypes: float64(2), int64(5), str(5)
# memory usage: 83.7 KB

# ---------------------------------------------------------------------------------------------

# 3º outro passo importante é a função describe()
# o describe() vai nos dar uma visão estatistica da tabela

print(df.describe())

#        PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
# count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
# mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
# std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
# min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
# 25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
# 50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
# 75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
# max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200

# ---------------------------------------------------------------------------------------------

