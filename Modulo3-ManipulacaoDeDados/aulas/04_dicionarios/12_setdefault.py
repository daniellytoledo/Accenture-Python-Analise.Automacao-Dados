# o default() é um método que verifica se uma chave existe no dicionário. se a chave já existe, ele não altera nada e retorna o valor atual, se a chave não existe, ele cria a chave com o valor informado e retorna esse valor

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# aqui, o setdefault acha a chave nome e então exibe o valor do dicionário, ele ignora o "giovanna". e aí retorna o que já existe dentro da chave nome
contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# aqui, como a chave "idade" não existe, ele adiciona ao dicionário, ou seja:
# se a chave existir - usa o valor existente
# se a chave não existir - cria a chave com o valor informado
contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}