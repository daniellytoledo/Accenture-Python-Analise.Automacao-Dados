# Modelos de regressão 

# Vamos utilizar o dataset House Prices, que contém caracteristicas de imóveis e seus preços. Nosso objetivo será prever o preço de uma casa a partir de suas carateristicas. Esse é um problema clássico de regressão.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# scikit-learn é uma das bibliotecas mais utilizadas pra machine learning em python

# train_test_split - para dividir o conjunto de dados em 2 partes, uma para treinar e outra para teste
from sklearn.model_selection import train_test_split

# LinearRegression - utilizada para ajustar o modelo de regressão linear
from sklearn.linear_model import LinearRegression

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
df = pd.read_csv(url)
df.head()

# Antes de treinar o modelo, precisamos preparar os dados

# remove valores ausentes
df = df.dropna()
# removendo a median_house_value porque é o que estamos tentando prever
x = df.drop("median_house_value", axis=1) 
# transforma categorias em representações numéricas
x = pd.get_dummies(x)
# corresponde à resposta do problema que é o valor mediano das casas
y = df["median_house_value"]

# dividindo em dados em duas colunas, um conjunto de treino e outro de teste
x_train, x_test, y_train, y_test = train_test_split(
    # teste size diz respeito à porcentagem que será usada para teste, sendo 20% teste
    # sendo 80% usado para treinar o modelo
    x, y, test_size=0.2, random_state=42 
) 

# Modelo de regressão linear
# A regressão linear assume que a variável resposta pode ser modelada como:
# y = β0 + β1x1 + β2x2 + ... +βpxp + E 
# onde:
# y é a variável resposta
# x1 são as variáveis explicativas
# β1 são os coeficientes do modelo
# E representa o erro aleatório

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# Resíduos do modelo
# Após treinar o modelo, podemos calcular os resíduos:
# ei = yi -^yi
# Esses redíduos são fundamentais para diagnosticar a qualidade do ajuste do modelo.

residuos = y_test - y_pred

# Diagnóstico gráfico dos resíduos

plt.figure(figsize=(6,5))
plt.scatter(y_pred, residuos)
plt.axhline(0, color="red")
plt.xlabel("Valores Preditos")
plt.ylabel("Resíduos")
plt.title("Resíduos vs Valores Preditos")

plt.show()
# o gráfico mostra os resíduos no vertical e os valores preditos no eixo horizontal, cada ponto representa um conjunto de dados e a linha vermelha representa o valor zero. quando um ponto tá próxima da linha significa que o modelo fez uma boa previsão e tá bastante próximo da real, e quando o ponto tá longe significa que o modelo cometeu erros maiores daquela observaão

#--------------------------------------------------------------------------------------

# Distribuição dos resíduos

plt.figure(figsize=(6,5))
sns.histplot(residuos, kde=True)
plt.title("Distribuição dos Resíduos")
plt.show()

#--------------------------------------------------------------------------------------

# Métrica: Mean Absolute Error (MAE)
# Ele mede o erro médio em uma unidades da variável resposta. Interpretação: Em média, o modelo erra aproximadamente MAE unidades.

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
print(mae) # 50413.433308100575 em média que as previsões do modelo diferem  do valor real das observações

#--------------------------------------------------------------------------------------

# Métrica: Mean Squared Error (MSE)
# Diferentemente do MAE, o MSE penaliza mais fortemente erros grandes. Isso ocorre porque o erro é elevado ao quadrado.

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print(mae) # 4802179538.604137

#--------------------------------------------------------------------------------------

# Métrica: Root Mean Squared Error (RMSE)
# Permite interpretar o erro na mesma unidade da variável resposta.

from sklearn.metrics import root_mean_squared_error

rmse = np.sqrt(mse)
print(rmse) # np.float64(69297.71669113015)

#--------------------------------------------------------------------------------------

# Métrica: Mean Absolute Percentage Erro (MAPE)
# Essa métrica expressa o erro em percentual.

mape = np.mean(np.abs((y_test - y_pred) / y_test) * 100)
print(mape) # np.float64(28.5959744711941) que signigica que o modelo apresenta erro de 28,60% em relação ao valor real das casas

#--------------------------------------------------------------------------------------

# Coeficiente de Determinação
# Enquanto as métricas anteriores vão medir diretamente o tamanho do erro do modelo, essa mede quanto da variabilidade da variável resposta é explicada de fato pelo modelo ou não.

from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print(r2) # 0.6488402154432009 % da variabilidade do preço das caixas explicado pelas variáveis do modelo, ou seja, 35% restantes correspondem a fatores que o modelo não conseguiu capturar

#--------------------------------------------------------------------------------------

# Depois de aplicar todas essas métricas, podemos usar seus resultados para descrever o desempenho do modelo sobre uma perspectiva diferente. Principalmente dizer, se podemos melhorar o nosso modelo ou não. 65%, por exemplo, é um resultado ok, mas precisariamos fazer mais pré-tratamento para o modelo ficar mais sofisticado.

metrics = pd.DataFrame({
    "MAE": [mae],
    "MSE": [mse],
    "RMSE": [rmse],
    "MAPE": [mape],
    "R2": [r2]
})



