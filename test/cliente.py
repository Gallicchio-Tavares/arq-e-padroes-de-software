import ingredientes
from milkshake import Milkshake, MilkshakeChocolate, MilkshakeMorango, MilkshakeBanana, MilkshakeBaunilha, MilkshakeOvomaltine

class Cliente:
    @staticmethod
    def escolher_sabor() -> Milkshake:
        print("="*30)
        print("Boas vindas!")
        print("="*30)
        print("Escolha um sabor")
        print("1 - Chocolate")
        print("2 - Morango")
        print("3 - Banana")
        print("4 - Baunilha")
        print("5 - Ovomaltine")

        sabor = input("Escolha o sabor (1 a 5): ")
        try:
            sabor = int(sabor)
        except ValueError:
            print("Opção inválida. Escolhendo Chocolate por padrão.")
            sabor = 1

        if sabor == 1:
            return MilkshakeChocolate()
        elif sabor == 2:
            return MilkshakeMorango()
        elif sabor == 3:
            return MilkshakeBanana()
        elif sabor == 4:
            return MilkshakeBaunilha()
        elif sabor == 5:
            return MilkshakeOvomaltine()
        else:
            print("Opção inválida!")
            return MilkshakeChocolate()

    @staticmethod
    def add(ms: Milkshake, preco: float, descricao: str) -> None:
        adicionais = {
            1: ingredientes.Biscoito,
            2: ingredientes.Banana,
            3: ingredientes.Chantilly,
            4: ingredientes.Ouro,
            5: ingredientes.Trufa
        }

        b = True
        while b:
            print("Você vai querer algum topping? 0 se não quiser, 1 para biscoito, 2 para chantilly, "
                  "3 para gotas de chocolate, 4 para morango, 5 para paçoca")
            resposta = input("Escolha o topping (0 a 5): ")
            try:
                resposta = int(resposta)
            except ValueError:
                print("Escolha inválida. Tente novamente.")
                continue

            if resposta == 0:
                b = False
            elif resposta in adicionais:
                topping = adicionais[resposta]
                ms = topping(ms)
                preco += ms.preco()
                descricao += f", {ms.descricao()}"
            else:
                print("Escolha inválida. Tente novamente.")

        print(f"Seu milkshake ({descricao}) custa R${preco:.2f}")


if __name__ == "__main__":
    cliente = Cliente()
    sabor = cliente.escolher_sabor()
    preco_inicial = sabor.preco()
    descricao_inicial = sabor.descricao()
    cliente.add(sabor, preco_inicial, descricao_inicial)
