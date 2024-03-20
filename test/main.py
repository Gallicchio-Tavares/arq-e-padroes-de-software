from milkshake import MilkshakeChocolate, MilkshakeMorango, MilkshakeBanana, MilkshakeBaunilha, MilkshakeOvomaltine
from ingredientes import Ouro, Chantilly, Biscoito, Banana

if __name__ == "__main__":
    # Criando milkshakes com diferentes combinações
    milkshake1 = MilkshakeChocolate()
    print(f"{milkshake1.descricao()}: R${milkshake1.custo()}")

    milkshake2 = MilkshakeMorango()
    milkshake2 = Ouro(milkshake2)
    milkshake2 = Chantilly(milkshake2)
    print(f"{milkshake2.descricao()}: R${milkshake2.custo()}")

    milkshake3 = MilkshakeChocolate()
    milkshake3 = Banana(milkshake3)
    milkshake3 = Chantilly(milkshake3)
    milkshake3 = Biscoito(milkshake3)
    print(f"{milkshake3.descricao()}: R${milkshake3.custo()}")
