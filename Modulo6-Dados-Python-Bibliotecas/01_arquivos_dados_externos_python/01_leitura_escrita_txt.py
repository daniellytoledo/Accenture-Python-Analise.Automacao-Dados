# w - write | r - read | a - append

# criando um arquivo para teste

# escrever w
with open("dados.txt", "w") as arquivo:
    arquivo.write("Python é uma linguagem poderosa! \n")
    arquivo.write("Estamos aprendendo arquivos.")

# ler r
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
# Python é uma linguagem poderosa!
# Estamos aprendendo arquivos.

# -------------------------------------------------------------

# escrevendo um arquivo
with open("relatorio.txt", "w") as arquivo:
    arquivo.write("Relatório de vendas. \n")
    arquivo.write("Total: 1500")

# adicionando conteúdo ao arquivo
with open("relatorio.txt", "a") as arquivo:
    arquivo.write("\n Novo registro adicionado.")

# lendo linha por linha
with open("relatorio.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip()) # strip tira os espaços extras e quebras de linha