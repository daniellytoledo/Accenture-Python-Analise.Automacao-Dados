# Prevenção de Erros
# Sempre que possível devemos prevenir erros antes que aconteçam.

numero = input("Digite um número: ")

if numero.isdigit():     # isdigit verifica se o que foi digitado contém só dígitos (números) resultando em True ou False.
    numero = int(numero) # como o resultado de isdigit é True, então ele converte o dígito para número inteiro
    print(numero)        # e imprime a variável numero
else:
    print("Valor inválido.")

# Mensagens claras
# Mensagens de erro devem ser simples e claras para o usuário.

# Manutenção de código
# Um bom tratamento de exceções torna o código mais seguro, mais fácil de manter e mais fácil de depurar.