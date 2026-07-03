conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado) # 1 é o número em conjunto_a que não tem na conjunto_b

resultado = conjunto_b.difference(conjunto_a)
print(resultado) # 4 é o número em conjunto_b que não tem no conjunto_a