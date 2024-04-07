from tarefa import TarefaSimples, TarefaComposta


def imprimir_subtarefas(tarefa, nivel=0):
    if isinstance(tarefa, TarefaComposta):
        print(f"{' ' * nivel}Tarefa Composta: {tarefa.nome}")
        for subtarefa in tarefa.subtarefas:
            imprimir_subtarefas(subtarefa, nivel + 1)
    elif isinstance(tarefa, TarefaSimples):
        print(f"{' ' * nivel}Tarefa Simples: {tarefa.nome}")


def main():
    # Criando as tarefas
    tarefa1 = TarefaSimples("Varrer chão")
    tarefa2 = TarefaSimples("Arrumar cama")
    tarefa3 = TarefaSimples("Lustrar maçanetas")
    tarefa4 = TarefaSimples("Limpar janelas")
    tarefa5 = TarefaSimples("Tirar poeira")
    tarefa6 = TarefaSimples("Passar desinfetante")
    tarefa7 = TarefaSimples("Passar verniz")
    tarefa8 = TarefaSimples("Reorganizar armário")
    tarefa9 = TarefaSimples("Desentupir privada")
    tarefa10 = TarefaSimples("Limpar espelho")
    tarefa11 = TarefaSimples("Lavar chão")
    tarefa12 = TarefaSimples("Limpar pia")

    tarefa_composta1 = TarefaComposta("Limpar estante de livros")
    tarefa_composta1.adicionar_subtarefa(tarefa5)
    tarefa_composta1.adicionar_subtarefa(tarefa6)
    tarefa_composta1.adicionar_subtarefa(tarefa7)

    tarefa_composta2 = TarefaComposta("Limpar Quarto")
    tarefa_composta2.adicionar_subtarefa(tarefa_composta1)
    tarefa_composta2.adicionar_subtarefa(tarefa1)
    tarefa_composta2.adicionar_subtarefa(tarefa2)
    tarefa_composta2.adicionar_subtarefa(tarefa4)
    tarefa_composta2.adicionar_subtarefa(tarefa8)

    tarefa_composta3 = TarefaComposta("Limpar Banheiro")
    tarefa_composta3.adicionar_subtarefa(tarefa3)
    tarefa_composta3.adicionar_subtarefa(tarefa9)
    tarefa_composta3.adicionar_subtarefa(tarefa8)
    tarefa_composta3.adicionar_subtarefa(tarefa10)
    tarefa_composta3.adicionar_subtarefa(tarefa11)
    tarefa_composta3.adicionar_subtarefa(tarefa12)

    tarefa_composta4 = TarefaComposta("Limpar Casa")
    tarefa_composta4.adicionar_subtarefa(tarefa_composta2)
    tarefa_composta4.adicionar_subtarefa(tarefa_composta3)

    # Limpar Casa | -> Limpar Quarto -> Limpar estante -> tarefas simples (4 níveis)
    #             | -> Limpar Banheiro -> tarefas simples

    # Marcando algumas tarefas como concluídas
    tarefa1.marcar_concluida()
    tarefa2.marcar_concluida()
    tarefa3.marcar_concluida()
    tarefa4.marcar_concluida()
    tarefa5.marcar_concluida()
    tarefa6.marcar_concluida()

    print("\nTarefas:")
    for tarefa in [tarefa_composta4]:
        imprimir_subtarefas(tarefa)

    # Testando a conclusão de uma tarefa composta
    print("Estado das tarefas:")
    print(f"{tarefa1.nome}: Concluída? {tarefa1.esta_concluida()}")
    print(f"{tarefa2.nome}: Concluída? {tarefa2.esta_concluida()}")
    print(f"{tarefa5.nome}: Concluída? {tarefa5.esta_concluida()}")
    print(f"{tarefa6.nome}: Concluída? {tarefa6.esta_concluida()}")
    print(f"{tarefa10.nome}: Concluída? {tarefa10.esta_concluida()}")
    print(f"{tarefa11.nome}: Concluída? {tarefa11.esta_concluida()}")
    print(f"{tarefa_composta1.nome}: Concluída? {tarefa_composta1.esta_concluida()}")
    print(f"{tarefa_composta2.nome}: Concluída? {tarefa_composta2.esta_concluida()}")
    print(f"{tarefa_composta3.nome}: Concluída? {tarefa_composta3.esta_concluida()}")
    print(f"{tarefa_composta4.nome}: Concluída? {tarefa_composta4.esta_concluida()}")

    # Marcando uma tarefa composta como concluída
    print(f"\nMarcando a tarefa {tarefa_composta2.nome} como concluída...")
    tarefa_composta2.marcar_concluida()

    # desfazendo conclusões e removendo tarefas:
    tarefa5.desfazer_conclusao()
    tarefa_composta2.remover_subtarefa(tarefa1)

    print("\nEstado da tarefa Limpar Quarto:")  # removeu varrer chão
    for tarefa in [tarefa_composta2]:
        imprimir_subtarefas(tarefa)

    print("\nEstado das tarefas após marcar a tarefa composta 1 como concluída:")
    print(f"{tarefa1.nome}: Concluída? {tarefa1.esta_concluida()}")
    print(f"{tarefa2.nome}: Concluída? {tarefa2.esta_concluida()}")
    print(f"{tarefa3.nome}: Concluída? {tarefa3.esta_concluida()}")
    print(f"{tarefa4.nome}: Concluída? {tarefa4.esta_concluida()}")
    print(f"{tarefa5.nome}: Concluída? {tarefa5.esta_concluida()}")
    print(f"{tarefa6.nome}: Concluída? {tarefa6.esta_concluida()}")
    print(f"{tarefa7.nome}: Concluída? {tarefa7.esta_concluida()}")
    print(f"{tarefa8.nome}: Concluída? {tarefa8.esta_concluida()}")
    print(f"{tarefa9.nome}: Concluída? {tarefa9.esta_concluida()}")
    print(f"{tarefa10.nome}: Concluída? {tarefa10.esta_concluida()}")
    print(f"{tarefa11.nome}: Concluída? {tarefa11.esta_concluida()}")
    print(f"{tarefa12.nome}: Concluída? {tarefa12.esta_concluida()}")

    print(f"{tarefa_composta1.nome}: Concluída? {tarefa_composta1.esta_concluida()}")
    print(f"{tarefa_composta2.nome}: Concluída? {tarefa_composta2.esta_concluida()}")
    print(f"{tarefa_composta3.nome}: Concluída? {tarefa_composta3.esta_concluida()}")
    print(f"{tarefa_composta4.nome}: Concluída? {tarefa_composta4.esta_concluida()}")

    print("\nTodas as tarefas concluídas:")
    tarefa_composta4.marcar_concluida()
    print(f"{tarefa_composta3.nome}: Concluída? {tarefa_composta3.esta_concluida()}")
    print(f"{tarefa_composta4.nome}: Concluída? {tarefa_composta4.esta_concluida()}")


if __name__ == "__main__":
    main()
