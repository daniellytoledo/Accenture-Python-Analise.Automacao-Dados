conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# o conjunto_a está em conjunto_b? 
resultado = conjunto_a.issubset(conjunto_b)  
print(resultado) # True

# o conjunto_b está em conjunto_b?
resultado = conjunto_b.issubset(conjunto_a)  
print(resultado) # False