carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# usar enumerate para transformar a lista carros em uma sequência de pares (índice, valor)
# se formos usar apenas "for indice, carro in carros" daria erro como se indice e carro fossem variáveis com o mesmo resultado 
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
