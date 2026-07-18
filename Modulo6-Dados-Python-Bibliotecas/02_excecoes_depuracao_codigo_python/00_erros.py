# O que são erros?

# Durante a execuçâo de um programa podem corror erros inesperados: Esses erros sâo chamados de exceçôes: Eles acontecem quando o Python encontra uma situaçâo que nâo consegue executar: Exemplos:

# dividir um número por zero
# acessar um arquivo que não existe
# converter texto para número de forma incorreta

numero = 10/0
print(numero) # ZeroDivisionError: division by zero

num = int("abc") # tentando transformar letras em número inteiro, obviamente dará erro
print(num) # ValueError

# SyntaxError       - erro de sintaxe
# TypeError         - operação com tipo incorreto
# ValueError        - valor inválido
# FileNotFoundError - arquivo não encontrado

# --------------------------------------------------------------------------------------------------

# Try / Except

# O bloco try permite tentar executar um código. Se ocorrer um erro, o except captura esse erro. 

try:
    n = 10/0
    print(n)
except ZeroDivisionError:
    print("Erro: divisão por zero.")

# --------------------------------------------------------------------------------------------------

# Finally

# O bloco finally executa independentemente de ocorrer erro ou não.

try:
    n = int("10") # 10 dado como string, então a conversão ocorre
except ValueError:
    print("erro de conversão!") # o print não executa porque não houve erro
finally:
    print("Execução finalizada.") # o finally é executado dando erro ou não no try, então o print é executado

# --------------------------------------------------------------------------------------------------

# RAISE

# A palavra raise permite gerar um erro manualmente.

idade = -5
if idade < 0:
    raise ValueError("Idade não pode ser negativa!")

# --------------------------------------------------------------------------------------------------

# Depuração (Debugging)

# Depurar significa encontrar e corrigir eros no código.
# Print Debugging: uma forma simles de depurar é usar print() para verificar valores.