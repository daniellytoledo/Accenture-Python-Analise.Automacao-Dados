conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# verificando se o conjunto_a contém todos os elementos do conjunto_b
resultado = conjunto_a.issuperset(conjunto_b)  
print(resultado) # False

# verificando se o conjunto_b contém todos os elementos do conjunto_a
resultado = conjunto_b.issuperset(conjunto_a)  
print(resultado) # True