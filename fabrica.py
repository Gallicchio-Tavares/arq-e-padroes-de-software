from abc import ABC, abstractmethod
from personagens import Guerreiro, Mago, Arqueiro, Clerigo, Bardo, Personagem

# Classe fábrica de personagens
class FabricaPersonagem(ABC):
    @abstractmethod
    def criar_personagem(self) -> Personagem:
        pass

# Fábricas concretas para cada classe de personagem
class FabricaGuerreiro(FabricaPersonagem):
    def criar_personagem(self) -> Personagem:
        return Guerreiro()

class FabricaMago(FabricaPersonagem):
    def criar_personagem(self) -> Personagem:
        return Mago()

class FabricaArqueiro(FabricaPersonagem):
    def criar_personagem(self) -> Personagem:
        return Arqueiro()

class FabricaClerigo(FabricaPersonagem):
    def criar_personagem(self) -> Personagem:
        return Clerigo()

class FabricaBardo(FabricaPersonagem):
    def criar_personagem(self) -> Personagem:
        return Bardo()
