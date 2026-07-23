# Redução de Complexidade

# Evite código muito complicado. Prefira:

# Funções simples
# Código dividido em partes

# O que é performance?

# Performance é a velocidade e eficiência do código.

# Profiling

# Profiling é analisar o desempenho do código.

import time

inicio = time.time()

for i in range(10000):       # simulação de quanto tempo leva pra esse loop terminar
    pass

fim = time.time()

print("Tempo: ", fim - inicio)

#----------------------------------------------------------------------------------

# exemplo com lista

numeros = list(range(10000000))
soma = sum(numeros)
print(soma)

#------------------------------------------------------------------------------------

# Projeto final

# Vamos aplicar tudo: organização, função reutilizável, teste, performance

def calcular_total_vendas(vendas):
    return sum(vendas)

dados = [100, 200, 300, 400]
resultado = calcular_total_vendas(dados)

print("Total: ", resultado)

