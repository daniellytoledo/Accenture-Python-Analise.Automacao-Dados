# CSV
# arquivos CSV são usados para representar tabelas de dados. usado para planilhas, análise de dados, exportação de sistemas
# criando um arquivo CSV

import csv

print("\n")
print("ARQUIVO CSV")
print("\n")

dados_csv = [
    ["nome", "idade", "cidade"],
    ["Ana",    25,    "São Paulo"],
    ["Carlos", 30,    "Rio de Janeiro"],
    ["Maria",  28,    "Belo Horizonte"]
]

# newline="" utilizado pra evitar linhas em branco no arquivo csv
with open("pessoas.csv", "w", newline="") as arquivo:
    writer = csv.writer(arquivo) # obj responsável por escrever os dados no arquivo
    writer.writerows(dados_csv)      # writerows escreve todas as linhas da lista dados  no arquivo csv de uma vez

# ler
with open("pessoas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

# -------------------------------------------------------------------------------------

# JSON
# JSON é um formato usado para armazenar e transmitir dados estruturados. Muito usado para APIs, aplicações web, armazenamento de dados...

import json

print("\n")
print("ARQUIVO JSON")
print("\n")

dados_json = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

with open("usuario.json", "w") as arquivo:
    json.dump(dados_json, arquivo) # recebe duas informaçoes: os dados e onde salvar

# lendo o json
with open("usuario.json", "r") as arquivo:
    dados_json = json.load(arquivo)
print(dados_json)
