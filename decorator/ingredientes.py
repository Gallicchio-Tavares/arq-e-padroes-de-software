from milkshake import Milkshake


# decorator para ingredientes adicionais
class IngredienteDecorator(Milkshake):
    def __init__(self, milkshake: Milkshake) -> None:
        self._milkshake = milkshake

    def preco(self) -> float:
        pass

    def descricao(self) -> str:
        pass


# ingredientes concretos
class Biscoito(IngredienteDecorator):
    def preco(self) -> float:
        return 5.0

    def descricao(self) -> str:
        return "pedaços de Oreo"


class Banana(IngredienteDecorator):
    def preco(self) -> float:
        return 2.0

    def descricao(self) -> str:
        return "rodelas de banana"


class Chantilly(IngredienteDecorator):
    def preco(self) -> float:
        return 3.0

    def descricao(self) -> str:
        return "chantilly"


class Ouro(IngredienteDecorator):
    def preco(self) -> float:
        return + 1000.0

    def descricao(self) -> str:
        return "folhas de ouro"


class Trufa(IngredienteDecorator):
    def preco(self) -> float:
        return + 430.0

    def descricao(self) -> str:
        return "trufa branca"
