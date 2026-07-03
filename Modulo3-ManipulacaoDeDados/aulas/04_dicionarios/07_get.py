contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

# nesse get o resultado é none porque o get tá buscando um elemento chamado "chave", ou seja, não existe nenhum elemento chave nesse dicionário
resultado = contatos.get("chave")  
print(resultado) # None 

# nesse get o resultado é vazio porque o get tá querendo buscar uma "chave" e seu dicionário, mas como esse elemento chave não existe, ele apenas volta o conjunto {} em vazio
resultado = contatos.get("chave", {})  
print(resultado) # {}

# por isso que aqui, o resultado já aparece, o get busca por uma chave existente e seu dicionário, então ele devolve a chave, nesse caso sendo "guilherme@gmail.com" e em seguida tudo que está dentro da chave
resultado = contatos.get(
    "guilherme@gmail.com", {}
)  
print(resultado) # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}