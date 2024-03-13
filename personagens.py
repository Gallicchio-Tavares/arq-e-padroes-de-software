from abc import ABC, abstractmethod

# Interface comum para classes de personagens
class Personagem(ABC):
    @abstractmethod
    def habilidade(self):
        pass

    @abstractmethod
    def equipamento(self):
        pass

# Classes de personagens concretas
class Guerreiro(Personagem):
    def habilidade(self):
        return {"ataque": "Corpo a corpo", "defesa": "Bloqueio"}

    def equipamento(self):
        return "Espada e armadura"

class Mago(Personagem):
    def habilidade(self):
        return {"ataque": "Magia de fogo", "defesa": "Escudo mágico"}

    def equipamento(self):
        return "Cajado e robe"

class Arqueiro(Personagem):
    def habilidade(self):
        return {"ataque": "Ataque à distância", "defesa": "Esquiva"}

    def equipamento(self):
        return "Arco e flechas"

class Clerigo(Personagem):
    def habilidade(self):
        return {"ataque": "Poder de velocidade", "defesa":"Poder de cura"}

    def equipamento(self):
        return "Capa protetora"

class Bardo(Personagem):
    def habilidade(self):
        return {"ataque": "Cacofonia ensurdecedora", "defesa": "Campo de Força sonoro"}

    def equipamento(self):
        return "Viola e harpa"