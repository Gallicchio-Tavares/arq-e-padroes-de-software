from milkshake import Milkshake

# Decorator para ingredientes adicionais
class IngredienteDecorator(Milkshake):
    def __init__(self, milkshake: Milkshake) -> None:
        self._milkshake = milkshake

    def preco(self) -> float:
        pass

    def descricao(self) -> str:
        pass

# Ingredientes concretos
class Biscoito(IngredienteDecorator):
    def preco(self) -> float:
        return self._milkshake.preco() + 5.0

    def descricao(self) -> str:
        return self._milkshake.descricao() + ", pedaços de Oreo"

class Banana(IngredienteDecorator):
    def preco(self) -> float:
        return self._milkshake.preco() + 2.0

    def descricao(self) -> str:
        return self._milkshake.descricao() + ", rodelas de banana"

class Chantilly(IngredienteDecorator):
    def preco(self) -> float:
        return self._milkshake.preco() + 3.0

    def descricao(self) -> str:
        return self._milkshake.descricao() + ", chantilly"

class Ouro(IngredienteDecorator):
    def preco(self) -> float:
        return self._milkshake.preco() + 1000.0

    def descricao(self) -> str:
        return self._milkshake.descricao() + ", folhas de ouro"

class Trufa(IngredienteDecorator):
    def preco(self) -> float:
        return self._milkshake.preco() + 430.0

    def descricao(self) -> str:
        return self._milkshake.descricao() + ", trufa branca"
