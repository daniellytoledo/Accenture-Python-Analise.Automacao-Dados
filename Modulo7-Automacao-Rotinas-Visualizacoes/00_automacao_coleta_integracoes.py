# Conceito de Automação

# Automação é o processo de executar tarefas automaticamente usando programas. Em vez de executar tarefas manualmente, criamos scripts que realizam essas tarefas de forma automática. Isso permite:

# economizar tempo
# reduzir erros
# processar grandes volumes de dados

# Cenários reais de automação

# A automação é usada em várias áreas:

# geração automática de relatórios
# coleta de dados da internet
# processamento diário de arquivos
# atualização de banco de dados
# monitoramente de sistemas

# Python é muito usado para automação por ser simples e poderoso.

# Manipulação automatizada de arquivos

# Uma das automações mais comuns é processar arquivos automaticamente. Por exemplo:

# ler arquivos de dados
# calcular métricas
# gerar relatórios

import csv

# criando arquivo de vendas
total = 0
with open("vendas.txt", "w") as f:
    f.write("100 \n 200 \n 150 \n 300 ")

with open("vendas.txt", "r") as f:
    for linha in f:
        valor = int(linha.strip())
        total += valor

print("Total de vendas: ", total)

# ------------------------------------------------------------------------------------------

# Integração com APIs e bancos
# Uma API permite que sistemas compartilhem dados automaticamente.Podemos usar APIs para coletar dados da internet.

import requests

url = "https://api.agify.io/?name=ana"

resposta = requests.get(url)
dados    = resposta.json()

print(dados)