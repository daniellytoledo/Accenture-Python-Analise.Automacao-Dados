contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# o pop removeu a chave, mas também devolve o valor dessa chave
resultado = contatos.pop("guilherme@gmail.com")  
print(resultado) # {'nome': 'Guilherme', 'telefone': '3333-2221'}

# o pop neste caso, remove a chave guilherme@gmail.com e em seguida pede o que está dentro dela, mas como ela foi removida do dicionário, ou seja, não existe, o resultado volta como vazio {} porque o código pediu 
resultado = contatos.pop("guilherme@gmail.com", {})  
print(resultado) # {}