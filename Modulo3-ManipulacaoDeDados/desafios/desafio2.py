# Desafio
# Você foi contratado por uma biblioteca digital que deseja organizar seu acervo de livros de forma eficiente. Cada livro é identificado por um título e um código único. Para facilitar buscas rápidas, a equipe decidiu armazenar os dados em um dicionário, onde a chave é o título do livro e o valor é o código correspondente. Sua tarefa é ajudar a equipe a encontrar o código de um livro a partir do seu título, utilizando as estruturas de dados apropriadas.

# Implemente um programa que leia uma lista de pares título-código, seguida de um título de livro a ser consultado. O programa deve retornar o código correspondente ao título informado. Caso o título não exista no acervo, retorne a mensagem Livro nao encontrado. Utilize apenas estruturas de dados básicas, como arrays e dicionários, sem bibliotecas externas.

# Entrada
# A primeira linha contém um número inteiro N, indicando a quantidade de livros cadastrados. As próximas N linhas contêm cada uma um título e um código separados por espaço. A última linha contém o título do livro a ser consultado.

# Saída
# Imprima o código correspondente ao título consultado. Caso o título não exista, imprima Livro nao encontrado.

# Leitura da quantidade de livros cadastrados
n = int(input())

# Dicionário para armazenar o acervo: título -> código
acervo = {}

# Leitura dos pares título-código
for _ in range(n):
    linha = input().strip() # aqui o usuário cadastra as linhas que foram determinadas no n sobre o livro,
    titulo, codigo = linha.split() # o split separa o titulo e o codigo em 2 valores ["titulo", "codigo"]
    # aqui é adicionado ao dicionário acervo, o título [titulo] que tem o valor igual ao código, ou seja, no dicionário fica então assim { "titulo": "codigo"}
    acervo[titulo] = codigo
    # TO DO: Separe o título e o código da linha e adicione ao dicionário 'acervo'
    # Dica: Use split() para separar e atribua corretamente no dicionário
    

# Leitura do título a ser consultado
consulta = input().strip()

# Busca pelo título no acervo e impressão do resultado
if consulta in acervo:
    print(acervo[consulta])
else:
    print("Livro nao encontrado")