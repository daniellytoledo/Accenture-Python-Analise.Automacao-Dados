conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# verificando se o conjunto_a NÃO possue nenhum elemento em comum com o conjunto_b
resultado = conjunto_a.isdisjoint(conjunto_b)  
print(resultado) # True

# verificando se o conjunto_a NÃO possue nenhum elemento em comum com o conjunto_c
resultado = conjunto_a.isdisjoint(conjunto_c)  
print(resultado) # False: possui o número 1 em comum