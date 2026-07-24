# Avaliação de Modelos de Classificação

# Em muitos problemas de ciências de dados, o objetivo não é prever um valor contínuo, mas sim classificar observações em categorias. Exemplo:

# fraude vs não fraude
# churn  vs não churn
# doença vs saudável
# spam   vs não spam

# Para avaliar modelos de classificação, utilizamos métricas baseadas nas comparações entre classes reais e classes previstas.

# Vamos transformar o dataset de regressão em classificação.
# Objetivo: classificar em preço alto vs preço baixo

# Avaliação de Modelos de Classificação

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# -------------------------------------------------------------------
# Carregando os dados

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

df = pd.read_csv(url)

# Remove linhas com valores ausentes
df = df.dropna()

# -------------------------------------------------------------------
# Criando a variável de classificação

# 1 = preço acima da mediana
# 0 = preço abaixo ou igual à mediana

# compara o preço da casa com o mediano do valor do preço das casas
df["HighPrice"] = (
    df["median_house_value"] >
    df["median_house_value"].median()
).astype(int)

print(df.head())

# -------------------------------------------------------------------
# Separando variáveis de entrada (X) e saída (y)

X = df.drop(["median_house_value", "HighPrice"], axis=1)

# Converte colunas categóricas em numéricas
X = pd.get_dummies(X)

y = df["HighPrice"]

# Dividindo treino e teste

# teste size diz respeito à porcentagem que será usada para teste, sendo 20% teste
# sendo 80% usado para treinar o modelo
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------------------------------------------
# Regressão Logística

# A regressão logística modela a probabilidade de pertencimento a uma classe.
# O modelo estima a probabilidade de um evento ocorrer.

clf = LogisticRegression(max_iter=1000)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# -------------------------------------------------------------------
# Matriz de Confusão

# A matriz de confusão compara valores reais e valores previstos. Ela possui quatro componentes fundamentais:

# TP: True Positive  → previu 0 e realmente era 0
# TN: True Negative  → previu 1, mas era 0
# FP: False Positive → previu 0, mas era 1
# FN: False Negative → previu 1 e realmente era 1

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))

sns.heatmap(
    cm,           # É a matriz de confusão.
    annot=True,   # Escreve os números dentro de cada quadrado.
    fmt="d",      # Significa que os valores são inteiros (d = decimal integer).
    cmap="Blues"  # Usa uma escala de azul. Quanto maior o número, mais escuro será o quadrado.
)

plt.xlabel("Classe Predita")
plt.ylabel("Classe Real")
plt.title("Matriz de Confusão")

plt.show()

#------------------------------------------------------------------------------------
# Acurácia

# Acurária mede a proporção total de previsões corretas.
# Interpretação: Qual a fração das previsões do miodelo está correta?

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

#------------------------------------------------------------------------------------
# Precision

# Precision responde à pergunta: das previsões feitas pelo modelo, quantas estavam corretas?
# Essa métrica é especialmente importante quando falsos positivos são custosos.

from sklearn.metrics import precision_score

precision = precision_score(y_test, y_pred)
print(precision)

#------------------------------------------------------------------------------------
# Recall

# Recall responde à pergunta: dos casos positivos reais, quantos foram identificados pelo modelo?
# Essa métrica é fundamental quando falsos negativos são perigosos.

from sklearn.metrics import recall_score

recall = recall_score(y_test, y_pred)
print(recall) 
# o resultado é em porcentagem

#------------------------------------------------------------------------------------
# F1 Score

# O F1-Score combina precision e recall em uma única métrica.
# Ele é definido como a média harmônica entre as duas métricas. É útil quando queremos equilibrar:
# falsos positivos
# falsos negativos

from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred)
print(f1)

#------------------------------------------------------------------------------------
# Classificação

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

#------------------------------------------------------------------------------------
# Conclusão

# Cada métrica responde a uma pergunta diferente:

# Accuracy  → qual taxa geral de acertos?
# Precision → quantas previsões positivas estavam corretas?
# Recall    → quantos positivos foram detectados?
# F1-score  → equilíbrio entre precision e recall

