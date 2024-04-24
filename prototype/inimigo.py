import copy
from random import randint

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def clone(self):
        return copy.deepcopy(self)

    def atacar(self, target) -> None:
        pass

class Bruxo(Enemy):
    def __init__(self):
        super().__init__("Bruxo", 50, 10)

    def atacar(self, target) -> None:
        print(f"{self.name} lança um feitiço em {target.name}!")
        target.health -= self.damage

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 100, 20)

    def atacar(self, target) -> None:
        print(f"{self.name} ataca {target.name} com um machado!")
        target.health -= self.damage

class Esqueleto(Enemy):
    def __init__(self):
        super().__init__("Esqueleto", 30, 15)

    def atacar(self, target) -> None:
        print(f"{self.name} ataca {target.name} com uma espada!")
        target.health -= self.damage
