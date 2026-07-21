# Integração com banco de dados

# Também podemos automatizar o armazenamento de dados em bancos de dados.

import sqlite3

conn   = sqlite3.connect("dados.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EISTS usuarios (
    nome TEXT,
    idade INT
    )
""")

conn.commit()

print("Tabela criada com sucesso!")

cursor.execute(
    "INSERT INTO usuarios VALURES (?, ?)",
    ("Ana", 25)
)

conn.commit()

print("Usuário inserido com sucesso!")

cursor.execute("SELECT * FROM usuarios")
dados = cursor.fetchall()

print("Usuários no banco: ")

for usuario in dados:
    print(usuario)


conn.close()
print("Conexão com o banco encerrada.")