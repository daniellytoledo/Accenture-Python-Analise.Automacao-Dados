# Em programação, herança é a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base).

# Benefícios:
# Representa bem os relacionamentos do mundo real.
# Fornece reutilização de código, não precisamos escrever o mesmo código repetidamente. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
# É de natureza transitiva, o que significa que, se a classe B herdar da classe A, todas as subclasses de B herdarão automaticamente da classe A.

# Herança simples
# Quando uma classe filha herda apenas uma classe pai.

# class A:
#   pass

# class B(A)

# Herança múltipla
# Quando uma classe filha herda de várias classes pai.

# class A:
#   pass

# class B:
#   pass

# class C(A, B): # classe C sendo filha da classe A e classe B
#   pass

