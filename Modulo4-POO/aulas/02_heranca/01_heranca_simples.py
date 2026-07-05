class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor          = cor
        self.placa        = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor...")

    def __str__(self):
        return self.cor

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        # o super serve para puxar as caracteristicas atribuidas no init, sem ele aqui, vai dar erro no print(caminhao) porque a cor não tá sendo puxada pelo pai da classe 
        super().__init__(cor, placa, numero_rodas) 
        self.carregado = carregado
        
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado.")

# se formos criar uma moto, ele já puxa quais atributos que tem que ser passados
moto = Motocicleta("preta", "abc-1234", 2)
print(moto)
moto.ligar_motor()

print("\n")

carro = Carro("branco", "xde-1684", 4)
carro.ligar_motor()

print("\n")

caminhao = Caminhao("roxo", "dsd-5784", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(caminhao)

# se formos tentar chamar a função esta_carregado do caminhao por outra classe, não vai funcionar porque essa função está dentro de caminhão