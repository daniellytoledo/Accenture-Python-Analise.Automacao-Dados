contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos  
print(resultado) # True

resultado = "megui@gmail.com" in contatos  
print(resultado) # False

resultado = "idade" in contatos["guilherme@gmail.com"]  
print(resultado) # False

resultado = "telefone" in contatos["giovanna@gmail.com"]  
print(resultado) # True