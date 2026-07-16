# Integração com bando de dados e APIs

# O que é uma API?
# API significa Application Programming Interface. Permite que um sistema forneça dados para outro sistema, ou seja, em vez de acessar diretamente um banco de dados ou arquivo, podemos pedir informações para um serviço na internet. Exemplos:

# previsão do tempo
# dados de criptomoedas
# dados de usuários
# mapas e localização

# Normalmente as APIs retornam dados no formato JSON.

# --------------------------------------------------------------------------------------

# Requisições HTTP

# Para acessar uma API precisamos fazer uma requisição HTTP.
# O tipo mais comum é o GET - usado para buscar dados. Em Python usamos a biblioteca requests para fazer requisições.

import requests

# api pra ver idade de alguém aleatoriamente
url = "https://api.agify.io/?name=danielly"
resposta = requests.get(url)
print(resposta.status_code) # 200 (requisição realizada com sucesso)
print(resposta.text)        # {"count":180,"name":"danielly","age":31}

print("\n")
print("-"*40)
print("\n")

# Leitura de dados externos (API)

# A maioria das APIs retorna dados no formado JSON. Podemos converter diretamente para um dicionário Python.

url = "https://api.agify.io/?name=danielly"
resposta = requests.get(url)
dados = resposta.json()
print(dados) # {"count":180,"name":"danielly","age":31}

print("\n")

print("Nome: ", dados["name"])
print("Idade Estimada: ", dados["age"])
print("Número de registros: ", dados["count"])

# --------------------------------------------------------------------------------------

# Salvando dados da API

# Depois de coletar dados de uma API, podemos salvar esses dados em um arquivo. Isso permite criar relatórios ou bases de dados locais.

print("\n")

import json

url = "https://api.agify.io/?name=danielly"
resposta = requests.get(url)
dados = resposta.json()

with open("dados_api.json", "w") as arquivo:
    json.dump(dados, arquivo)

# --------------------------------------------------------------------------------------

# Integração com bando de dados

# Além de arquivos, também podemos armazenar dados em banco de dados. Um banco de dados permite:

# armazenar grandes quantidades de informação
# organizar dados em tabelas
# consultar dados rapidamente

# Em Python podemos usar vários bancos de dados. Vamos usar SQLite

# criando uma conexão com o banco

print("\n")

import sqlite3

conexao = sqlite3.connect("dados.db") # cria o banco de dados
cursor = conexao.cursor()             # cria a conexao
cursor.execute("""                    # executa o comando, cria uma tabela
    CREATE TABLE usuarios(
        nome TEXT,
        idade INT
    )
""")

conexao.commit() # salva as alterações

cursor.execute(
    "INSERT INTO usuarios VALUES (?, ?)"
    ("Ana", 25)
)

conexao.commit() # salva as alterações

cursor.execute("SELECT * FROM usuarios") # seleciona tudo da tabela usuários
dados = cursor.fetchall()                # cria a variável dados, sendo igual ao resultado do select
print(dados)

# --------------------------------------------------------------------------------------

# Automatizando importação e exportação de dados

# Em muitos sistemas, os dados precisam ser processados automaticamente. Por exemplo:

# ler um arquivo de vendas todos os dias
# processar os dados
# gerar um relatório
# salvar os resultados

# Esse processo automático é chamado de automação de dados. Muitas empresas utilizam esse tipo de automação para:

# análise de dados
# relatórios automáticos
# integração entre sistemas