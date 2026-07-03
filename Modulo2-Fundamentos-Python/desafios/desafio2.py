# Desafio
# Você foi contratado por uma consultoria para auxiliar uma empresa do setor financeiro a automatizar a validação de transações bancárias. Cada transação possui um valor e uma taxa de serviço. O sistema precisa calcular o valor final da transação (valor menos taxa) e verificar se o valor final é suficiente para cobrir um pagamento mínimo exigido pela empresa. Caso o valor final seja igual ou superior ao pagamento mínimo, a transação é aprovada; caso contrário, é recusada. Sua tarefa é implementar essa lógica utilizando operadores e expressões em Python, garantindo que o sistema seja confiável e preciso para o negócio.

# Implemente um programa que leia três números inteiros: o valor da transação, a taxa de serviço e o pagamento mínimo. Calcule o valor final da transação subtraindo a taxa do valor. Se o valor final for maior ou igual ao pagamento mínimo, imprima "Aprovada". Caso contrário, imprima "Recusada".

# Leitura dos três valores inteiros em uma única linha
entrada = input()
valor_transacao, taxa_servico, pagamento_minimo = map(int, entrada.split())

# Calcule o valor final da transação subtraindo a taxa do valor
# valor_final = ...

valor_final = valor_transacao - taxa_servico

# Verifique se o valor final é suficiente para aprovar a transação
if valor_final >= pagamento_minimo:
    print("Aprovada")
else:
    print("Recusada")