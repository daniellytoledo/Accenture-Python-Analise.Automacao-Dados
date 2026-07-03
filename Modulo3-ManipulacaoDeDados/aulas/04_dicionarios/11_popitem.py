contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "danielly@gmail.com": {"nome": "Dani", "telefone": "3333-2221"}
}

# o popitem neste caso vai eliminar o último item que foi adicionado ao dicionário, que neste caso eu coloquei danielly. então ele remove o último item adicionado e guarda esse valor
resultado = contatos.popitem()  
print(resultado) # ('danielly@gmail.com', {'nome': 'Dani', 'telefone': '3333-2221'})

# contatos.popitem()  # KeyError