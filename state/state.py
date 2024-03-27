class State:
    def __init__(self, central):
        self.central = central

    def confirmar(self):
        raise NotImplementedError()

    def preparar(self):
        raise NotImplementedError()

    def entregar(self):
        raise NotImplementedError()

    def concluir(self):
        raise NotImplementedError()

    def set_state(self, novo_estado):
        self.central.set_estado(novo_estado)


class PedidoConfirmado(State):
    def __init__(self, central):
        super().__init__(central)

    def confirmar(self):
        print("Pedido confirmado!\n")

    def preparar(self):
        self.central.set_estado(Preparando(self.central))
        print("Seu pedido está sendo preparado!\n")

    def entregar(self):
        print("Pedido ainda não confirmado...\n")

    def concluir(self):
        print("Pedido ainda não confirmado...\n")


class Entregando(State):
    def __init__(self, central):
        super().__init__(central)

    def confirmar(self):
        print("O pedido está a caminho\n")

    def preparar(self):
        print("O pedido está a caminho\n")

    def entregar(self):
        print("O pedido está a caminho\n")

    def concluir(self):
        self.central.set_estado(None)
        print("Entrega finalizada!\n")


class Preparando(State):
    def __init__(self, central):
        super().__init__(central)

    def confirmar(self):
        print("O pedido está sendo preparado\n")

    def preparar(self):
        print("O pedido está sendo preparado\n")

    def entregar(self):
        self.central.set_estado(Entregando(self.central))
        print("A pessoa que fará a entrega já está a caminho do seu endereço!\n")

    def concluir(self):
        print("O pedido ainda está sendo preparado\n")


class Aguardando(State):
    def __init__(self, central):
        super().__init__(central)

    def confirmar(self):
        self.central.set_estado(PedidoConfirmado(self.central))
        print("O restaurante confirmou o pedido!\n")

    def preparar(self):
        print("Pedido ainda não confirmado...\n")

    def entregar(self):
        print("Pedido ainda não confirmado...\n")

    def concluir(self):
        print("Pedido ainda não confirmado...\n")
