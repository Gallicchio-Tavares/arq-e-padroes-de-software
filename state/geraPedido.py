import time
from state import Aguardando

class CentralDePedidos:
    def __init__(self):
        self.estado = None

    def set_estado(self, estado):
        self.estado = estado

    def pedir(self):

        metodos_pagamento = {
            1: 'Cartão de Crédito',
            2: 'Cartão de Débito',
            3: 'Pix',
            4: 'Dinheiro'
        }

        print("Escolha o método de pagamento:")
        print(f'''
            [1] {metodos_pagamento[1]}
            [2] {metodos_pagamento[2]}
            [3] {metodos_pagamento[3]}
            [4] {metodos_pagamento[4]} (10% de desconto)
        ''')

        a = True

        while a:
            try:
                resposta = int(input())
                if resposta in metodos_pagamento:
                    print(f"Opção de pagamento com \033[35m{metodos_pagamento[resposta]}\033[m selecionada\n")
                    a = False  #pra sair do loop
                else:
                    print("Por favor insira uma opção válida.\n")
            except ValueError: # pessoa não digita um int
                print("Por favor insira uma opção válida.\n")


        self.set_estado(Aguardando(self))
        time.sleep(1)

        self.estado.confirmar()
        time.sleep(1)

        self.estado.preparar()
        time.sleep(5)

        self.estado.entregar()
        time.sleep(3)

        self.estado.concluir()
