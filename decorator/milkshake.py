from abc import ABC, abstractmethod


# componente base - Milkshake
class Milkshake(ABC):  # classe abstrata
    @abstractmethod
    def preco(self) -> float:
        pass

    @abstractmethod
    def descricao(self) -> str:
        pass


# sabores base de Milkshake
class MilkshakeChocolate(Milkshake):
    def preco(self) -> float:
        return 7.0

    def descricao(self) -> str:
        return "Milkshake de Chocolate"


class MilkshakeMorango(Milkshake):
    def preco(self) -> float:
        return 5.0

    def descricao(self) -> str:
        return "Milkshake de Morango"


class MilkshakeOvomaltine(Milkshake):
    def preco(self) -> float:
        return 10.0

    def descricao(self) -> str:
        return "Milkshake de Ovomaltine"


class MilkshakeBanana(Milkshake):
    def preco(self) -> float:
        return 5.0

    def descricao(self) -> str:
        return "Milkshake de Banana"


class MilkshakeBaunilha(Milkshake):
    def preco(self) -> float:
        return 7.0

    def descricao(self) -> str:
        return "Milkshake de Baunilha"
