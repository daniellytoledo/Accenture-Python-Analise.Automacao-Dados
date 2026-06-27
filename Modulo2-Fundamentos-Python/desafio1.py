# Desafio
# Você foi contratado por uma consultoria especializada em soluções para o varejo. Sua primeira missão é automatizar o sistema de promoções de uma grande rede de lojas. O sistema deve analisar o valor total da compra de um cliente e, de acordo com regras de negócio, decidir qual benefício será aplicado. Dependendo do valor, o cliente pode ganhar um desconto, um brinde ou apenas uma mensagem de agradecimento. Sua tarefa é implementar a lógica que, a partir do valor da compra, determina e exibe a mensagem correta para cada situação, garantindo que o sistema funcione de forma automática e sem erros.

# Implemente um programa que leia o valor total da compra (um número inteiro representando reais) e, usando estruturas condicionais, imprima uma das seguintes mensagens:
# - Se o valor for menor que 50, imprima "Obrigado por comprar conosco!"
# - Se o valor for de 50 a 99 (inclusive), imprima "Parabens! Voce ganhou um brinde!"
# - Se o valor for de 100 a 199 (inclusive), imprima "Desconto de 10 reais aplicado!"
# - Se o valor for 200 ou mais, imprima "Desconto de 25 reais aplicado!"

# Lê o valor total da compra como inteiro
valor_compra = int(input())

# Implemente a estrutura condicional para decidir e imprimir a mensagem correta
# Dica: Use if, elif e else para comparar o valor_compra com as faixas especificadas no enunciado.

if valor_compra < 50:
  print("Obrigado por comprar conosco!")
elif 50 <= valor_compra <= 99:
  print("Parabéns! Você ganhou um brinde!")
elif 100 <= valor_compra <= 199:
  print("Desconto de 10 reais aplicado!")
else:
  print("Desconto de 25 reais aplicado!")