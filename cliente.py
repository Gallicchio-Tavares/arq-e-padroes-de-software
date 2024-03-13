from fabrica import FabricaGuerreiro, FabricaMago, FabricaArqueiro, FabricaBardo, FabricaClerigo

class Cliente:
    def criar_personagem(self, fabrica):
        personagem = fabrica.criar_personagem()
        print(f"Personagem criado: \033[34m{type(personagem).__name__}\033[m")
        habilidade = personagem.habilidade()
        print(f"Ataque: \033[31m{habilidade['ataque']}\033[m")
        print(f"Defesa: \033[32m{habilidade['defesa']}\033[m")
        print(f"Equipamento: \033[36m{personagem.equipamento()}\033[m")
        print()
        return personagem

cliente = Cliente()

guerreiro = FabricaGuerreiro()
cliente.criar_personagem(guerreiro)

mago = FabricaMago()
cliente.criar_personagem(mago)

arqueiro = FabricaArqueiro()
cliente.criar_personagem(arqueiro)

clerigo = FabricaClerigo()
cliente.criar_personagem(clerigo)

bardo = FabricaBardo()
cliente.criar_personagem(bardo)