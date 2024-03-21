from abc import ABC, abstractmethod


# Componente base - Milkshake
class Milkshake(ABC):  # esse eh o component, é uma classe abstrata
    @abstractmethod
    def preco(self) -> float:
        pass

    @abstractmethod
    def descricao(self) -> str:
        pass


# Sabores base de Milkshake
class MilkshakeChocolate(Milkshake):  # como se fosse o concrete component
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
