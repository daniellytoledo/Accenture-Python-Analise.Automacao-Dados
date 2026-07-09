# Polimorfismo na Herança

# Na herança, a classe filha herda os métodos da classe pai. No entando, é possível modificar um método em uma classe filha herdada da classe pai. Isso é particulamente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha.

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar.")

# exemplo ruim de exemplo de herança para ganhar o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião decolando...")

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())

plano_voo(Aviao())