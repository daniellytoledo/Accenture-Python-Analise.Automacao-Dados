# Avaliação de Modelos de Agrupamento

# Diferentemente de regressão e classificação, no clustering não temos rótulos verdadeiros. Ou seja:
# não sabemos a resposta correta
# não sabemos quantos grupos realmente existem

# O objetivo do clustering é descobrir padrões estruturais nos dados. Exemplos:

# segmentação de clientes
# padrões de consumo
# agrupamento de documentos
# segmentação de imagens

# Como não temos rótulos verdadeiros, precisamos avalisar os clusters usando critérios internos. Esses critérios geralmente medem duas propriedades:
# 1. Coesão   → quão próximo estão os pontos dentro de um cluster
# 2. Sepração → quão distante estão clusters diferentes

#-----------------------------------------------------------------------------------
# Preparando dados para clustering

# Vamos utilizar o mesmo dataset usado anteriormente (California Housing)
# Para clustering, selecionaremos apenas algumas variáveis numéricas:

# median_income
# housing_median_age
# total_rooms

# Antes de aplicar algoritmos de agrupamento, é importante padronizar as variáveis, pois muitas métricas utiliam distância euclidiana. 

#----- 

# Within Sum of Squares (WSS)
# WSS mede a variabilidade dentro dos clusters. Interpretação: valores menores indicam clusters mais compactos.

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

wss = []
K   = range(1, 10)

for k in K:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(X_cluster)        # faltou mostrar o código todo na aula

    wss.append(model.inertia_)

# resultado do método do cotovelo, ajuda na escolha do número adequado de clusters
plt.plot(K, wss, marker="o")
plt.xlabel("Número de clusters")
plt.ylabel("WSS")
plt.title("Elbow Method")

plt.show()

#-----------------------------------------------------------------------------------
# Índice Calinski-Harabasz

# O índice de Calinski-Harabasz mede a razão entre dispersão entre clusters e dispersão dentro dos clusters. Interpretação: valores maiores indicam clusters melhores.
# Se os clusters estiverem bem definidos, podemos esperar que cada grupo esteja relativamente próximo entre si, isso seria uma baixa dispersão. Ao mesmo tempo que os diferentes clusters estejam bem separados um do outro.

#-----------------------------------------------------------------------------------
# Índice de Silhueta

# O índice de silhueta combina coesão e separação. Valores possíveis:

# próximo de 1 → clusters bem definidos
# próximo de 0 → clusters sobrepostos
# negativo     → cluster mal definido

from sklearn.metrics import silhouette_score

silhueta = silhouette_score(X_cluster, clusters)
print(silhueta)
# resultado em porcentagem

#-----------------------------------------------------------------------------------
# Davies-Boudin Index

# Esse índice mede a relação entre dispersão interna e distância entre clusters.
# Interpretação: valores menores indicam clusters melhores.

from sklearn.metrics import davies_bouldin_score

db = davies_bouldin_score(X_cluster, clusters)
print(db)

#-----------------------------------------------------------------------------------
# Dunn Index

# O índice Dunn mede a razão entre menor distância entre clusters e maior diâmetro dentro de um cluster.
# Interpretação: valores maiores indicam clusters melhores.

from scipy.spatial.distance import cdist
import numpy as np

def dunn_index(X, labels):
    clusters = np.unique(labels)
    centroids = np.array([X[labels == k].mean(axis=0) for k in clusters])
    intercluster = np.min(cdist(centroids, centroids) + np.eye(len(centroids)) * 1e9)

    intracluster = np.max([
        np.max(cdist(X[labels == k], X[labels == k]))
        for k in clusters
    ])

    return intercluster / intracluster

dunn = dunn_index(X_cluster.values, clusters)
print(dunn)

#-----------------------------------------------------------------------------------

# Comparação das métricas

cluster_metrics = pd.DataFrame({
    "WSS":               [KMeans.inertia_],
    "Calinski-Harabasz": [silhueta],
    "Davies-Bouldin":    [db],
    "Dunn":              [dunn]
})

