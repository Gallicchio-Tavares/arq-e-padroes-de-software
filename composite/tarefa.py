from abc import ABC, abstractmethod
from typing import List


class Tarefa(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.concluida = False

    @abstractmethod
    def marcar_concluida(self):
        pass

    @abstractmethod
    def desfazer_conclusao(self):
        pass

    def esta_concluida(self):
        return self.concluida


class TarefaSimples(Tarefa):
    def marcar_concluida(self):
        self.concluida = True

    def desfazer_conclusao(self):
        self.concluida = False


class TarefaComposta(Tarefa):
    def __init__(self, nome):
        super().__init__(nome)
        self.subtarefas: List[Tarefa] = []

    def adicionar_subtarefa(self, subtarefa: Tarefa):
        self.subtarefas.append(subtarefa)

    def remover_subtarefa(self, subtarefa: Tarefa):
        self.subtarefas.remove(subtarefa)

    def marcar_concluida(self):
        for subtarefa in self.subtarefas:
            subtarefa.marcar_concluida()
        self.concluida = True

    def desfazer_conclusao(self):
        for subtarefa in self.subtarefas:
            subtarefa.desfazer_conclusao()
        self.concluida = False

