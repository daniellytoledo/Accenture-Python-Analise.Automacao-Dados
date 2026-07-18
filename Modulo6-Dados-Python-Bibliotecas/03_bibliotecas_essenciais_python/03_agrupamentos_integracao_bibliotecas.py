import pandas as pd

dados = {
    "produtos": ["Notebook", "Mouse", "Teclado"],
    "preco": [3500, 120, 150]
}

df = pd.DataFrame(dados)
print(df.groupby("produtos").mean()) # cada produto aparece uma única vez, caso repetido e o mean calcula a média de cada grupo

import matplotlib.pyplot as plt

produtos = ["Notebook", "Mouse", "Teclado"]
vendas = [15, 50, 30]

plt.bar(produtos, vendas)
plt.show()