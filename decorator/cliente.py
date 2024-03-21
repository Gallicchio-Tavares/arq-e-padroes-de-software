import ingredientes
import milkshake


class Cliente:
    @staticmethod
    def escolher_sabor() -> milkshake.Milkshake:
        print("=" * 30)
        print("Boas vindas!")
        print("=" * 30)

        print("Escolha um sabor")
        print("1 - Chocolate")
        print("2 - Morango")
        print("3 - Banana")
        print("4 - Baunilha")
        print("5 - Ovomaltine")

        while True:
            try:
                tipo = int(input("Escolha o sabor! "))
                if tipo in range(1, 6):
                    if tipo == 1:
                        return milkshake.MilkshakeChocolate()
                    elif tipo == 2:
                        return milkshake.MilkshakeMorango()
                    elif tipo == 3:
                        return milkshake.MilkshakeBanana()
                    elif tipo == 4:
                        return milkshake.MilkshakeBaunilha()
                    elif tipo == 5:
                        return milkshake.MilkshakeOvomaltine()
                else:
                    print("Opção inválida. Escolha um número entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    @staticmethod
    def add(escolha_cliente: milkshake.Milkshake, preco: float, descricao: str) -> None:
        comp = ""
        com = ""
        adicionais = {
            1: ingredientes.Biscoito,
            2: ingredientes.Banana,
            3: ingredientes.Chantilly,
            4: ingredientes.Ouro,
            5: ingredientes.Trufa
        }

        b = True
        while b:
            print("Escolha um complemento!")
            num = input("[1] Pedaços de Oreo\n[2] Banana\n[3] Chantilly\n[4] Folhas "
                        "de Ouro\n[5] Trufa Branca\n[0] Finalizar\n")
            try:
                num = int(num)
            except ValueError:
                print("Por favor, digite um número.")
                continue

            if num == 0:
                b = False
            elif num in adicionais:
                complemento = adicionais[num]
                escolha_cliente = complemento(escolha_cliente)
                preco += escolha_cliente.preco()
                com = "com"
                comp += f"{escolha_cliente.descricao()}, "
            else:
                print("Escolha inválida. Tente novamente.")

        print(f"Seu {descricao} {com} {comp}custa R${preco:.2f}")


if __name__ == "__main__":
    cliente = Cliente()
    sabor = cliente.escolher_sabor()
    preco_inicial = sabor.preco()
    descricao_inicial = sabor.descricao()
    cliente.add(sabor, preco_inicial, descricao_inicial)
