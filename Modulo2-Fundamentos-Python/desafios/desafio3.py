# Desafio
# Você faz parte da equipe de transformação digital de uma consultoria que está integrando dados de diferentes sistemas legados. Cada sistema armazena nomes de clientes de formas variadas: alguns usam letras maiúsculas, outros minúsculas, e há casos em que nomes vêm com espaços extras no início ou no fim. Para garantir a padronização e facilitar a análise, sua tarefa é criar um programa que normalize esses nomes, removendo espaços desnecessários e ajustando a capitalização de acordo com o padrão: a primeira letra de cada palavra deve ser maiúscula e as demais, minúsculas.

# Implemente um programa que receba uma string representando o nome de um cliente, possivelmente com letras em qualquer caixa e espaços extras no início ou no fim. O programa deve retornar o nome formatado corretamente, com apenas um espaço entre as palavras e cada palavra iniciando com letra maiúscula.

# Entrada
# Uma única linha contendo uma string representando o nome de um cliente, que pode conter letras maiúsculas ou minúsculas e espaços extras no início ou no fim.

# Saída
# Uma única linha contendo o nome do cliente formatado: cada palavra deve começar com letra maiúscula, as demais letras devem ser minúsculas, e deve haver apenas um espaço entre as palavras, sem espaços extras no início ou no fim.

# Lê a entrada do usuário (nome do cliente)
entrada = input()

# Remove espaços extras no início/fim e divide em palavras
palavras = entrada.strip().split()

# Capitaliza cada palavra
palavras_formatadas = [palavra.capitalize() for palavra in palavras]

# Junta as palavras com um único espaço
nome_formatado = ' '.join(palavras_formatadas)

# Exibe o nome formatado
print(nome_formatado)