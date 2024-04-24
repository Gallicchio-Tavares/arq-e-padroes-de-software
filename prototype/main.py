from random import randint
from inimigo import Orc, Bruxo, Esqueleto

class Cliente:
    def __init__(self):
        self.enemies = []

    def create_enemies(self):
        bruxo = Bruxo()
        orc = Orc()
        esqueleto = Esqueleto()

        # Clonar inimigos para criar mais instâncias com pequenas diferenças
        bruxo2 = bruxo.clone()
        bruxo2.name = "Voldemort"
        bruxo2.health += 50

        orc2 = orc.clone()
        orc2.name = "Ragash"
        orc2.damage += 10

        self.enemies.extend([bruxo, orc, esqueleto, bruxo2, orc2])

    def print_enemies(self):
        for enemy in self.enemies:
            print(f"{enemy.name}: Saúde - {enemy.health}, Dano - {enemy.damage}")

    def simular_batalha(self):
        while len(self.enemies) > 1:
            for enemy in self.enemies:
                target = self.enemies.copy()
                target.remove(enemy)
                target = target[randint(0, len(target) - 1)]
                enemy.atacar(target)
                if target.health <= 0:
                    print(f"{target.name} foi derrotado!")
                    self.enemies.remove(target)
            print("-----------")
        print(f"{self.enemies[0].name} é o vencedor da batalha!")

if __name__ == "__main__":
    client = Cliente()
    client.create_enemies()
    client.print_enemies()
    client.simular_batalha()
