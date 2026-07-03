# o remove elimina um elemento do conjunto ou de uma lista, mas ele elimina a primeira ocorrência desse elemento caso tenha elementos repetidos. 

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

# como está dentro de um set{}, vai ser mostrado os números sem os repetidos
print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# o resultado desse código é None porque ele não tem o que mostrar, o que está dentro de print é apenas um comando para remover o elemento 0 do conjunto, ou seja, ele executa esse comando e pronto, não há nada para ser mostrado no print
print(numeros.remove(0))  # None

# aqui sim já mostra que o 0 foi removido porque estamos printando apenas o conjunto
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}